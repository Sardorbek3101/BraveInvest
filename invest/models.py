from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    black_theme = models.BooleanField(default=False)
    profile_picture = models.ImageField(blank=True, null=True)


class Book(models.Model):
    title = models.CharField(max_length=200)
    cover_picture = models.ImageField()
    description = models.TextField()
    pdf = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title
    

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    about = models.TextField()
    picture = models.ImageField()

    def __str__(self):
        return f"{ self.first_name } {self.last_name}"
    

class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} {self.author.first_name} {self.author.last_name}"
    

class Mentorship(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    video_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

def strip_double_quotes(quoted_string):
    return quoted_string.replace('"', '')


class InvestingCourses(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    video_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
