from rest_framework import generics
from .models import Book
from .serializers import BookSerializers

class BookListcreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookDetail(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
