from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    code_content = models.TextField()
    language = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
