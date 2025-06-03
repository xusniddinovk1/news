from django_filters import rest_framework as django_filters
from core.models import Category, Post


class NewsFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__slug', lookup_expr='iexact')
    created_at = django_filters.DateFromToRangeFilter()
    is_published = django_filters.BooleanFilter()

    class Meta:
        model = Post
        fields = ['category', 'created_at', 'is_published']