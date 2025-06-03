from core.pagination import CustomPagination
from core.serializers import CategorySerializers, PostSerializers
from core.models import Category, Post
from core.permissions import IsStaffOrReadOnly, IsOwnerOrReadOnly
from rest_framework import generics

class CategoryListCreateViewSet(generics.ListCreateAPIView):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Category.objects.alL()
    serializer_class = CategorySerializers

    pagination_class = CustomPagination