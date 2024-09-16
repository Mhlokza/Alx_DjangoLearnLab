from django.urls import path
from blog import views 

urlpatterns = [
    path('login/'),
    path('logout/'),
    path('register/', views.RegisterView.as_view(), name= 'login'),
    path('profile/'),
    ["post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/"]
]
