from django.shortcuts import render

# Create your views here.

from datetime import date
from uuid import uuid4

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from .serializers import CertificateSerializer


# Temporary in-memory storage; not persistent.
CERTIFICATES = []
NEXT_CERTIFICATE_ID = 1


def public_certificate(certificate):
    return {
        key: value
        for key, value in certificate.items()
        if key != "user_id"
    }


class CertificateListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="List My Certificates",
        responses=CertificateSerializer(many=True),
    )
    def get(self, request):
        certificates = [
            public_certificate(item)
            for item in CERTIFICATES
            if item["user_id"] == request.user.pk
        ]
        return Response({
            "count": len(certificates),
            "certificates": certificates,
        })

    @extend_schema(
        summary="Issue a Certificate",
        request=CertificateSerializer,
    )
    def post(self, request):
        global NEXT_CERTIFICATE_ID

        serializer = CertificateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if data["issued_date"] > date.today():
            return Response(
                {"issued_date": "Issued date cannot be in the future."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        certificate = {
            "id": NEXT_CERTIFICATE_ID,
            "user_id": request.user.pk,
            **data,
            "certificate_code": f"SS-{uuid4().hex[:12].upper()}",
            "status": data.get("status", "Issued"),
        }

        CERTIFICATES.append(certificate)
        NEXT_CERTIFICATE_ID += 1

        return Response(
            public_certificate(certificate),
            status=status.HTTP_201_CREATED,
        )


class CertificateDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_certificate(self, request, certificate_id):
        return next(
            (
                item for item in CERTIFICATES
                if item["id"] == certificate_id
                and item["user_id"] == request.user.pk
            ),
            None,
        )

    @extend_schema(
        summary="Get Certificate Details",
        responses=CertificateSerializer,
    )
    def get(self, request, certificate_id):
        certificate = self.get_certificate(request, certificate_id)

        if certificate is None:
            return Response(
                {"detail": "Certificate not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(public_certificate(certificate))

    @extend_schema(summary="Delete My Certificate")
    def delete(self, request, certificate_id):
        certificate = self.get_certificate(request, certificate_id)

        if certificate is None:
            return Response(
                {"detail": "Certificate not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        CERTIFICATES.remove(certificate)

        return Response(
            {"message": "Certificate deleted successfully."},
            status=status.HTTP_200_OK,
        )
