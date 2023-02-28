from django.db import models
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    title = models.CharField(max_length=200)
    cover_picture = models.ImageField()
    description = models.TextField()
    pdf = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title
    

# class User(AbstractUser):
#     black_theme = models.BooleanField(default=False)
