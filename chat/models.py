from django.db import models


# Create your models here.
class Chat(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    difficulty = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
