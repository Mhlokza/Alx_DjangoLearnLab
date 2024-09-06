from .models import Book, Author 
from rest_framework import serializers

class BookSerializer(serializers.BookSerializer):
    class Meta:
        model = Book
        fiels = ['title','publication_year','author']

class AuthorSerializer(serializers.Serializer):
    class Meta:
        model = Author
        field = 'name'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title','publication_year','author']

    def validate(self, data):
        if not (data['publication_year']) < datetime.now():
            raise serializers.ValidationError("publication time cannot be in the future")
        return data