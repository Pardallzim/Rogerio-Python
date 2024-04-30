from django.urls import path
from turma.views import *

urlpatterns = [
    path('', index, name='index'),
    path('pagina/',pagina,name='pagina')
]