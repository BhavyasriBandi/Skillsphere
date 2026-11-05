from rest_framework import serializers


class SupportTicketSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    subject = serializers.CharField(max_length=200)

    category = serializers.ChoiceField(
        choices=[
            "Technical Issue",
            "Account Problem",
            "Career Guidance",
            "Learning Resource",
            "Other",
        ]
    )

    description = serializers.CharField(max_length=2000)

    priority = serializers.ChoiceField(
        choices=["Low", "Medium", "High"],
        default="Medium"
    )

    status = serializers.ChoiceField(
        choices=["Open", "In Progress", "Resolved"],
        read_only=True
    )

    created_at = serializers.DateTimeField(read_only=True)