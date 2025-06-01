from rest_framework import serializers
from core.models import Category, Post


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
