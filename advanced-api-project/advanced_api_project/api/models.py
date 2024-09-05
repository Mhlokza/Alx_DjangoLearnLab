from django.db import models
from rest_framework import serializers
from datetime import datetime
from .models import BlogPost

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='product')

class BookSerializer(serializers.BookSerializer):
    class Meta:
        model = Book
        fiels = '__all__'

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

    
