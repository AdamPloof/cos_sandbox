from django.forms import ModelForm
from .models import ArtworkCollection, ArtWork

class CollectionForm(ModelForm):
    class Meta:
        model = ArtworkCollection
        fields = [
            'collection_name',
            'collection_types',
        ]
        labels = {
            'collection_name': 'Collection Name'
        }

class ArtWorkForm(ModelForm):
    class Meta:
        model = ArtWork
        fields = [
            'title',
            'description',
            'created_date',
            'collection',
        ]
