import os
import asyncio
from dotenv import load_dotenv
from removebg import RemoveBg
from PIL import Image
from rest_framework import serializers
from .models import Plant, Category

load_dotenv()

class PlantSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    image = serializers.ImageField(write_only=True)
    
    class Meta:
        model = Plant
        fields = '__all__'
        
    def get_image_url(self, obj):
        request = self.context.get('request')
        
        if obj.image_url:
            return request.build_absolute_uri(obj.image_url)
        return None
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.image_url:
            representation['image_url'] = instance.image_url 

        return representation
        
    def create(self, validated_data):
        categories_data = validated_data.pop('categories', [])
        image = validated_data.pop('image', None)

        plant = Plant.objects.create(**validated_data)
        plant.categories.set(categories_data)

        if image:
            image_dir = f'media/{plant.id}'
            os.makedirs(image_dir, exist_ok=True)

            try:
                image_name = os.path.splitext(image.name)[0]
                temp_image_path = os.path.join(image_dir, f"{image_name}.png")
                processed_image_path = os.path.join(image_dir, f"{image_name}.png")

                img = Image.open(image)
                img.save(temp_image_path, format="PNG")

                asyncio.run(self.process_image(temp_image_path, image_name))

                os.remove(temp_image_path)

                plant.image_url = processed_image_path + "_no_bg.png"
                plant.save()

            except Exception as e:
                print(f"Error processing image: {e}")

        return plant
    
    async def process_image(self, temp_image_path, image_name):
        rmbg = RemoveBg(os.getenv('API_KEY_REMOVEBG'), "error.log")
        await asyncio.to_thread(rmbg.remove_background_from_img_file, temp_image_path)
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
