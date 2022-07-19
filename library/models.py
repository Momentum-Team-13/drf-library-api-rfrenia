from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"


class Book(models.Model):
    title = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")
    author = models.CharField(max_length=100, null=True, blank=True)
    publication_date = models.DateTimeField(null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    featured = models.BooleanField

    def __str__(self):
        return self.title
