pythonCopy codefrom django.urls import path 
from .views import BookListCreatAPIView

urlspattens = [path("api/books", views.BookListCreateAPIView.as_view(), name="book_list_create"),]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet


router = DefaultRouter()
router.register(r'my-models', MyModelViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(" ",api.urls),
    path((DefaultRouter()), router.urls, include),
    path("DefaultRouter(),router.urls, include", api.BookViewSet.),
    path('api/', include(router.urls)),
]