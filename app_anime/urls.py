from django.urls import path

from . import views

urlpatterns = [
    path("", views.serve_anime, name="index"),
]