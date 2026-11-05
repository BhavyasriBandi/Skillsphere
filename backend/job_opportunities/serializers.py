from rest_framework import serializers


class JobOpportunitySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(max_length=150)
    company = serializers.CharField(max_length=150)
    career_path = serializers.CharField(max_length=100)

    required_skills = serializers.ListField(
        child=serializers.CharField(max_length=100)
    )

    experience_level = serializers.ChoiceField(
        choices=[
            "Fresher",
            "Entry Level",
            "Intermediate",
            "Experienced",
        ]
    )

    work_mode = serializers.ChoiceField(
        choices=["On-site", "Remote", "Hybrid"]
    )

    location = serializers.CharField(max_length=150)
    apply_url = serializers.URLField(
        required=False,
        allow_blank=True
    )