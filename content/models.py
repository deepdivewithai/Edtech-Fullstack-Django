from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='content/')  # FileField for uploading files (e.g., PDFs, videos)
    # Other fields as needed, e.g., content type, author, timestamps, etc.

    def __str__(self):
        return self.title