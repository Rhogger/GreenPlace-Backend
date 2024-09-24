from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryListCreate, PlantImageView, PlantViewSet

router = DefaultRouter()
router.register(r'plants', PlantViewSet, basename='plants')

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('plants/<int:pk>/image/', PlantImageView.as_view(), name='plant-image'),
]
