from rest_framework import viewsets
from core.models import Category
from core.permissions import IsStaffOrReadOnly
from core.serializers import CategorySerializers


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializers