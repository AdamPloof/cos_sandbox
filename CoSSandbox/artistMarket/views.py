from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CollectionForm, ArtWorkForm

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
