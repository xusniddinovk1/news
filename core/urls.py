from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import CategoryViewSet, NewsListCreateViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'news', NewsListCreateViewSet)

urlpatterns = [
    path('', include(router.urls))
]
