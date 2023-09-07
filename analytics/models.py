from django.db import models
from user.models import Teacher

class AnalyticsData(models.Model):
    event_name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_name} by {self.teacher.name}"
