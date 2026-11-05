from rest_framework import serializers


class LeaderboardSerializer(serializers.Serializer):
    rank = serializers.IntegerField()
    student_id = serializers.IntegerField()
    student_name = serializers.CharField()
    completed_assessments = serializers.IntegerField()
    completed_goals = serializers.IntegerField()
    points = serializers.IntegerField()
