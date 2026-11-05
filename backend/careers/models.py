
from django.conf import settings
from django.db import models


class RoadmapTaskProgress(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="roadmap_task_progress",
    )
    career = models.CharField(max_length=100)
    task_id = models.CharField(max_length=255)
    task_name = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "career", "task_id"],
                name="unique_student_career_roadmap_task",
            )
        ]
        ordering = ["career", "task_id"]

    def __str__(self):
        return (
            f"{self.student_id} - {self.career} - "
            f"{self.task_name} ({'completed' if self.is_completed else 'pending'})"
        )
