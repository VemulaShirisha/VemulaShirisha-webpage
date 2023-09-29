from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
   path("realme/", views.realme),
   path("redme/", views.redme),
]