import os
from django.http import HttpResponse
from django.views import View
from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from common import settings

from .models import Plant, Category
from .serializers import PlantSerializer, CategorySerializer

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def post(self, request):
        serializer = PlantSerializer(data=request.data)
        
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        print(serializer.errors)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PlantImageView(View):
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(pk=pk)
            image_path = os.path.join(settings.BASE_DIR, plant.image_url)

            if os.path.exists(image_path):
                with open(image_path, 'rb') as image_file:
                    return HttpResponse(image_file.read(), content_type='image/png')
            else:
                return HttpResponse(status=404)
        
        except Plant.DoesNotExist:
            return HttpResponse(status=404)
    
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
