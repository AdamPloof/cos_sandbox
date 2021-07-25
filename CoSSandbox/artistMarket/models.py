from django.db import models
from django.contrib.auth.models import User

COLLECTION_TYPES = [
    ('album', 'Album'),
    ('collection', 'Collection'),
    ('show', 'Show'),
    ('suite', 'Suite'),
    ('bag', 'Bag'),
]

class ArtworkCollection(models.Model):
    collection_name = models.CharField(max_length=40)
    collection_types = models.CharField(max_length=40, choices=COLLECTION_TYPES)

    def __str__(self):
        return self.collection_name

class ArtWork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateField()
    published_date = models.DateField(auto_now_add=True)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    collection = models.ManyToManyField(ArtworkCollection)
    # image = models.ImageField()

    def __str__(self):
        return self.title