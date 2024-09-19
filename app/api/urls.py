from django.urls import path
from . import views

urlpatterns = [
    path('plants/', views.PlantListCreate.as_view()),
]