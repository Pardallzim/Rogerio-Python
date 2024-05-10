from django.urls import path
from turma.views import *

urlpatterns = [
    path('pagina/', index, name='index'),
    path('',pagina,name='pagina')
]