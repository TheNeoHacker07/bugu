from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=20)
    text = models.TextField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title