from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("georgi", views.georgi, name="georgi"),
    path("tedi", views.tedi, name="tedi")
]