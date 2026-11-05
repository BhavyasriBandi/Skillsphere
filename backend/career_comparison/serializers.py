from rest_framework import serializers


class CareerComparisonSerializer(serializers.Serializer):
    career_1 = serializers.CharField(max_length=100)
    career_2 = serializers.CharField(max_length=100)

    def validate(self, attrs):
        if (
            attrs["career_1"].strip().lower()
            == attrs["career_2"].strip().lower()
        ):
            raise serializers.ValidationError(
                "Please select two different careers."
            )

        attrs["career_1"] = attrs["career_1"].strip()
        attrs["career_2"] = attrs["career_2"].strip()

        return attrs