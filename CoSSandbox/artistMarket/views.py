from .models import ArtworkCollection
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CollectionForm, ArtWorkForm, CollectionSelectForm

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
            form.save()
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
