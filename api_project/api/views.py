from django.shortcuts import render
from rest_framework import generics.ListAPIView
from .models import Book
from .serializers import MyModelSerializer 
from .serializers import BookSerializer

class BookList(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    book_serializer = BookSerializer
 ["BookViewSet"]
 ["viewsets.ModelViewSet"]

 from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class MyAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Only authenticated users can access this view
        return Response({'message': 'Hello, authenticated user!'})