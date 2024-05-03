# from django.db import models
# from django.contrib.auth.models import User  # Using Django's User 

# class Comment(models.Model):
#     document = models.ForeignKey('documents.Document', on_delete=models.CASCADE)
#     line_number = models.IntegerField()
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_guest_comment = models.BooleanField(default=False)
#     guest_id = models.CharField(max_length=50, blank=True, null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
