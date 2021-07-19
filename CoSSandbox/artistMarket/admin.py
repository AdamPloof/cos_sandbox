from django.contrib import admin
from .models import ArtworkCollection, ArtWork

models = [
    ArtWork, 
    ArtworkCollection,
]

admin.site.register(models)
