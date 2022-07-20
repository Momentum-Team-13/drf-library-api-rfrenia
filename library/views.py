from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from .models import Book
from .serializers import BookSerializer


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        # "self" here is the instance of the view -- I can get to the request object through that!
        serializer.save(author=self.request.user)


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
