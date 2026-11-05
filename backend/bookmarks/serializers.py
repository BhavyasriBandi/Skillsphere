from rest_framework import serializers


class BookmarkSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    item_type = serializers.ChoiceField(
        choices=["Career", "Resource"]
    )

    item_id = serializers.IntegerField(min_value=1)

    title = serializers.CharField(
        max_length=200,
        required=False,
        allow_blank=True
    )

    url = serializers.URLField(
        required=False,
        allow_blank=True
    )

    created_at = serializers.DateTimeField(read_only=True)
