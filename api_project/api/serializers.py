from rest_framework import serializers
from .models import Book 

class BookSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = Book
        field = '__all__'
