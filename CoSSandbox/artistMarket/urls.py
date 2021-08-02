from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-collection', views.addCollection, name='add_collection'),
    path('add_artwork/<int:collectionId>', views.addArtwork, name='add_artwork'),
    path('select-collection/', views.selectCollection, name='select_collection'),
    path('generate-artworks/<int:numArtworks>', views.generateArtworks, name='generate_artworks'),
]
