
from rest_framework import serializers


class CertificateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    recipient_name = serializers.CharField(max_length=150)
    course_name = serializers.CharField(max_length=200)
    issued_date = serializers.DateField()
    certificate_code = serializers.CharField(read_only=True)
    status = serializers.ChoiceField(
        choices=["Issued", "Revoked"],
        default="Issued",
    )
