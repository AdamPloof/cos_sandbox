from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

import datetime

from .models import ArtworkCollection
from .forms import CollectionForm, ArtWorkForm, CollectionSelectForm
from .services.artworkGenerator import ArtworkGenerator

def index(request):
    context = {
        'page_title': 'Artist Home',
    }
    return render(request, 'index.html', context)

def addCollection(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            # Determine what the user wants to do next
            # Add flash message on collection save
            collection = form.save()
            messages.add_message(request, messages.SUCCESS, f'Collection added: {collection}')

            return HttpResponseRedirect(reverse('index'))
    else:
        form = CollectionForm()
    
    return render(request, 'add_collection.html', {'form': form})

def addArtwork(request, collectionId=None):
    if not collectionId:
        return HttpResponseRedirect(reverse('select_collection'))

    collection = ArtworkCollection.objects.get(pk=collectionId)

    if request.method == 'POST':
        form = ArtWorkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.artist_id = request.user.id
            artwork.save()
            artwork.collection.add(collection)

            artwork = form.save()
            messages.add_message(request, messages.SUCCESS, f'Artwork added: {artwork}')

            return HttpResponseRedirect(reverse('index'))
    else:
        form = ArtWorkForm(initial={'collection': collection})
    
    return render(request, 'add_artwork.html', {'form': form})

def selectCollection(request):
    if request.method == 'POST':
        form = CollectionSelectForm(request.POST, user=request.user)
        form.setCollectionNames()

        if form.is_valid():
            collectionName = form.cleaned_data['collection']
            collection = ArtworkCollection.objects.get(collection_name=collectionName)

            return HttpResponseRedirect(reverse('add_artwork', kwargs={'collectionId': collection.pk}))
    else:
        form = CollectionSelectForm(user=request.user)
        form.setCollectionNames()
    
    return render(request, 'select_collection.html', {'form': form})

def generateArtworks(request, numArtworks):
    if not numArtworks:
        # Should probably provide a flash message like, "must provide number of artworks"
        messages.add_message(request, messages.ERROR, 'Must provide number of artworks to add')
        return HttpResponseRedirect(reverse('index'))

    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2021, 1, 1)

    generator = ArtworkGenerator(start_date, end_date, request.user)

    try:
        generator.generateArtworks(numArtworks)
    except PermissionDenied as err:
        messages.add_message(request, messages.ERROR, 'Cannot generate artworks all willy-nilly. You must login first.')
        return HttpResponseRedirect(reverse('login'))


    messages.add_message(request, messages.SUCCESS, f'Generated {numArtworks} artworks!')

    return HttpResponseRedirect(reverse('index'))
