from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.image_create, name="image_create"),
    path("edit/<int:id>/", views.image_edit, name="image_edit"),
]
