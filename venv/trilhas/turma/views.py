from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import * 
# Create your views here.

def index(request):
    return HttpResponse('<h1>Olá Mundo.</h1>')

def pagina(request):
    return render(request,'index.html')

def variavel(request):
    form = UsuariosForm
    if request.method == "POST":
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()

    x = Usuarios.objects.all()

    return render(request, "var.html",{'users':x, 'form':form})

def itens(request):
    form = ItensForm
    if request.method == "POST":
        form = ItensForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    y = Itens.objects.all()

    return render(request, "itens.html",{'users':y, 'form':form})
