# Generated by Django 5.1.1 on 2024-09-23 17:20

from django.db import migrations

def seed_category(apps, schema_editor):
    Category = apps.get_model('api', 'Category')
    
    if Category.objects.count() == 0:
        categories = [
            'plant',
            'succulents',
            'tropical',
            'indoor',
            'outdoor',
            'lowlight',
            'flowering',
            'herbs',
            'vegetables',
            'ferns',
            'vines',
            'fruitBearing',
            ]
        for category in categories:
            Category.objects.create(name=category)
            
class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_category),
    ]
