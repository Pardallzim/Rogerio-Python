from django.urls import path
from . import views

urlpatterns = [
    path('pagina/', views.index, name='index'),
    path('', views.pagina, name='pagina'),
    path('variavel/', views.variavel, name='variavel'),
    path('cadastro/', views.variavel, name='cadastro'),
    path('itens/', views.itens, name='itens'),
]