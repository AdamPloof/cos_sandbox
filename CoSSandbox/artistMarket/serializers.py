from django.contrib.auth.models import User, Group
from .models import ArtworkCollection, ArtWork

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    artworks = serializers.PrimaryKeyRelatedField(many=True, queryset=ArtWork.objects.all())

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'artworks']


class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtWork
        fields = [
            'title',
            'description',
            'created_date',
            'published_date',
            'artist',
            'image',
        ]


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtworkCollection
        fields = [
            'id',
            'collection_name',
            'collection_types'
        ]
