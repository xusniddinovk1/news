from rest_framework import viewsets
from core.models import Category
from core.permissions import IsOwnerOrReadOnly
from core.serializers import CategorySerializers


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializers