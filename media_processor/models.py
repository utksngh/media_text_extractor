from django.db import models

from django.db import models

class ExtractedText(models.Model):
    file_name = models.CharField(max_length=255)
    content = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
