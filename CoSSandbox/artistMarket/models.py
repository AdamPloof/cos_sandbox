from django.db import models
from django.contrib.auth.models import User


class ArtworkCollection(models.Model):
    collection_name = models.CharField(max_length=40)

    
class ArtWork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateField
    published_date = models.DateField
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    collection = models.ManyToManyField(ArtworkCollection)
    image = models.CharField(max_length=200)
