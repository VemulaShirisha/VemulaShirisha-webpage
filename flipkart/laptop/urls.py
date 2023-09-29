from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path("dell/",views.dell),
    path("hp/",views.hp),

]