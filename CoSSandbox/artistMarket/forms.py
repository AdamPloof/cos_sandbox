from django.forms import ModelForm, Form, ChoiceField
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

class CollectionSelectForm(Form):
    collection = ChoiceField(
        label='Collection',
        choices=()
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CollectionSelectForm, self).__init__(*args, **kwargs)

    def setCollectionNames(self):
        collections = ArtworkCollection.objects.all()
        self.fields['collection'].choices = [(collection.collection_name, collection.collection_name )for collection in collections]
