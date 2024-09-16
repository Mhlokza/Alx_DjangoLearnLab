from django.urls import path
from blog import views 

urlpatterns = [
    path('login/'),
    path('logout/'),
    path('register/', views.RegisterView.as_view(), name= 'login'),
    path('profile/'),
    path('post/',<int:pk>/delete)
    path('post/',<int:pk>/update)
    path('post/', new)
]
