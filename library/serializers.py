from rest_framework import serializers
from .models import Book, User, Tracker


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["pk", "username", "email"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["pk", "title", "author", "publication_date", "genre", "featured_book"]


class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = ["pk", "want", "reading", "done"]