from django.shortcuts import render
from rest_framework import generics.ListAPIView
from .models import Book
from .serializers import MyModelSerializer 
from .serializers import BookSerializer

class BookList(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    book_serializer = BookSerializer
