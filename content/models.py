from django.db import models
from user.models import Teacher

class Content(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='content/') 

    def __str__(self):
        return f"{self.title} created by {self.teacher.name}"