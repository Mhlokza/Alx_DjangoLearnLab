from rest_framework import serializers
from .models import Book, Author, BlogPost
from datetime import datetime

#this serializirs the book model and validated the year
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = ['title','publication_year','author']


        def validate(self, data):
            if not (data['publication_year']) < datetime.now():
            raise serializers.ValidationError("Date must be not of the future")
            return data
#Author model serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        field = 'name'
#nested serializer
class BookSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True, read_only=True)
     class Meta:
        model = Book
        field = ['title','publication_year','author']



