from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from core.filters import NewsFilter
from core.pagination import CustomPagination
from core.serializers import CategorySerializers, PostSerializers
from core.models import Post
from core.permissions import IsStaffOrReadOnly
from rest_framework import viewsets


class NewsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Post.objects.filter(status='published').order_by('-created_at')
    serializer_class = PostSerializers
    lookup_field = 'slug'

    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_class = NewsFilter
    search_fields = ['title', 'context']
    ordering_fields = ['created_at']

    def get_queryset(self):
        queryset = Post.objects.all()
        if self.request.method == 'GET':
            queryset = queryset.filter(status='published')
        return queryset

    def list(self, request, *args, **kwargs):
        category = request.query_params.get('category', None)
        if category:
            self.queryset = self.queryset.filter(category=category)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        related_news = Post.objects.filter(category=instance.category).exclude(id=instance.id)[:3]
        related_serializer = PostSerializers(related_news, many=True)
        return Response({
            'news': serializer.data,
            'related_news': related_serializer.data
        })
