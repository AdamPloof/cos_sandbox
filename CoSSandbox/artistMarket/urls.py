from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-collection', views.addCollection, name='add_collection'),
]
