from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import CategoryViewSet, NewsViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
