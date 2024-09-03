from django.shortcuts import render
from rest_framework import generic
from .models import Book
from .serializers import MyModelSerializer

class BookList(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    BookViewSet = BookSerializer


