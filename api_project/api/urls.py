pythonCopy codefrom django.urls import path 
from .views import BookListCreatAPIView

urlspattens = [path("api/books", views.BookListCreateAPIView.as_view(), name="book_list_create"),]