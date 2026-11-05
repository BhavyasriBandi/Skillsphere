
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Portfolio
from .serializers import PortfolioSerializer


class PortfolioView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Return the logged-in student's portfolio.
        If no portfolio exists yet, return empty form data.
        """
        try:
            portfolio = Portfolio.objects.get(student=request.user)
        except Portfolio.DoesNotExist:
            return Response(
                {
                    "id": None,
                    "name": request.user.get_full_name() or "",
                    "headline": "Aspiring Software Developer",
                    "email": request.user.email or "",
                    "location": "",
                    "phone": "",
                    "objective": "",
                    "skills": (
                        "Python, Java, JavaScript, React, Django, SQL"
                    ),
                    "education": [],
                    "projects": [],
                    "certifications": "",
                    "resume_url": "",
                    "portfolio_url": "",
                    "github_url": "",
                    "linkedin_url": "",
                    "created_at": None,
                    "updated_at": None,
                },
                status=status.HTTP_200_OK,
            )

        serializer = PortfolioSerializer(portfolio)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        """
        Create or replace the logged-in student's portfolio.
        """
        serializer = PortfolioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        portfolio, created = Portfolio.objects.update_or_create(
            student=request.user,
            defaults=serializer.validated_data,
        )

        response_serializer = PortfolioSerializer(portfolio)

        return Response(
            {
                "message": (
                    "Portfolio saved successfully."
                    if created
                    else "Portfolio updated successfully."
                ),
                "portfolio": response_serializer.data,
            },
            status=(
                status.HTTP_201_CREATED
                if created
                else status.HTTP_200_OK
            ),
        )

    def patch(self, request):
        """
        Partially update the logged-in student's existing portfolio.
        """
        try:
            portfolio = Portfolio.objects.get(student=request.user)
        except Portfolio.DoesNotExist:
            return Response(
                {
                    "error": (
                        "Create your portfolio before updating it."
                    )
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = PortfolioSerializer(
            portfolio,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Portfolio updated successfully.",
                "portfolio": PortfolioSerializer(portfolio).data,
            },
            status=status.HTTP_200_OK,
        )

    def delete(self, request):
        """
        Delete only the logged-in student's portfolio.
        """
        try:
            portfolio = Portfolio.objects.get(student=request.user)
        except Portfolio.DoesNotExist:
            return Response(
                {"error": "Portfolio not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        portfolio.delete()

        return Response(
            {"message": "Portfolio deleted successfully."},
            status=status.HTTP_200_OK,
        )
