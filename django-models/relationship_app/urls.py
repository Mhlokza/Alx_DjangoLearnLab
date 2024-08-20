from django.urls import path
from .views import list_books, LibraryDetailView


urlpatterns = [
path('listbooks/', list_books, name = 'list_books'),
path('Librarydetail', LibraryDetailView.as_view(), name = 'library_detail')
[