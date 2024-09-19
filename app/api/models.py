from django.db import models

class Plant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.TextField()
    umidity = models.CharField(max_length=20)
    sunlight = models.CharField(max_length=20)
    categories = models.ManyToManyField('Category', blank=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name



#         class PlantModel {
#     def __init__(self, id, name, description, umidity, sunlight, categories=None, image_url=None):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.umidity = umidity
#         self.sunlight = sunlight
#         self.categories = categories if categories else []
#         self.image_url = image_url
# }