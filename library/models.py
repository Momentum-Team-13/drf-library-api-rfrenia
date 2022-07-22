from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    #is staff boolean

    def __str__(self):
        return f'{self.username} {self.email}'


class Book(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    publication_date = models.DateTimeField(null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    featured_Y = "Yes"
    featured_N = "No"
    featured_choices = [(featured_Y, "Yes"), (featured_N, "No")]
    featured_book = models.CharField(max_length=3, choices=featured_choices, default=featured_N,)
    owner = models.ForeignKey('User', related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def check_is_user_tracker(self, user):
        for tracker in self.trackers.all():
            if tracker.book == self:
                return True


class Tracker(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='trackers', null=True, blank=True)
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name='trackers', null=True, blank=True)
    want = "Want to Read"
    reading = "Currently Reading"
    done = "Read/Done"
    tracker_choices = [(want, "Want to Read"), (reading, "Currently Reading"), (done, "Read/Done")]

    def __str__(self):
        return f'{self.user}:{self.book}'
