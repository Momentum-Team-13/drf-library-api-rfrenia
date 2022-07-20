from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"


class Book(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    publication_date = models.DateTimeField(null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    featured_Y = "Yes"
    featured_N = "No"
    featured_choices = [(featured_Y, "Yes"), (featured_N, "No")]
    featured_book = models.CharField(max_length=3, choices=featured_choices, default=featured_N,)

    def __str__(self):
        return f'{self.title}'

    def check_is_user_tracker(self, user):
        for tracker in self.trackers.all():
            if tracker.book == self:
                return True


class Tracker(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='trackers', null=True, blank=True)
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name='trackers', null=True, blank=True)
    yes = "Yes"
    no = "No"
    tracker_choices = [(yes, "Yes"), (no, "No")]
    want = models.CharField(max_length=3, choices=tracker_choices, default=no,)
    reading = models.CharField(max_length=3, choices=tracker_choices, default=no,)
    done = models.CharField(max_length=3, choices=tracker_choices, default=no,)

    def __str__(self):
        return f'{self.user}:{self.book}'
