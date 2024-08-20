from django.urls import path
from .views import list_books, LibraryDetailView,register
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
path('listbooks/', list_books, name = 'list_books'),
path('Librarydetail', LibraryDetailView.as_view(), name = 'library_detail')
path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= "relationship_app/logout.html"), name='logout'),
    path('register/', views.register.as_view(), name = "register"),
[