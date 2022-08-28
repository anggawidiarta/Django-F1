from os import pathconf_names
from sys import path_importer_cache
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("v1", views.v1, name="v1"),
]