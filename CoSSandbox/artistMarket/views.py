from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'page_title': 'Artist Home',
    }
    return render(request, 'index.html', context)
