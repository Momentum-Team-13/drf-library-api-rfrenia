from rest_framework import serializers
from .models import Book, User, Tracker
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    trackers = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tracker.objects.all())

    class Meta:
        model = User
        fields = ("pk", "username", "trackers")


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ["pk", "title", "author", "publication_date", "genre", "featured_book", "owner", ]


class TrackerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def get_book_status(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Tracker
        fields = ["pk", "tracker_status", "owner", ]
