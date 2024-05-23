from django.urls import path
from siteSenai.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("usuarios/", usuarios, name="usuarios"),
    path("cards/", cards, name="cards"),
]