from django.urls import path, include
from core.serializers import CategorySerializers, PostSerializers
from rest_framework.routers import DefaultRouter
from core.views import *