from django.urls import path
from blog import views 

urlpatterns = [
    path('login/'),
    path('logout/'),
    path('register/', views.RegisterView.as_view(), name= 'login'),
    path('profile/'),
]