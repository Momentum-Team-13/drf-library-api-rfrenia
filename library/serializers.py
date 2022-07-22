from rest_framework import serializers
from .models import Book, User, Tracker
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ("pk", "username", "books")


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ["pk", "title", "author", "publication_date", "genre", "featured_book", "owner", ]


class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = ["pk", "tracker_choices", ]
