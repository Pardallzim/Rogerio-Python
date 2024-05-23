from django.shortcuts import render, redirect
from .forms import *
from .models import * 

# Create your views here.

def inicio(request):
    card = Cards.objects.all()
    return render(request, 'site/index.html',{"info":card})

def cards(request):
    form = CardsForm
    if request.method == "POST":
        form = CardsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
        return redirect('inicio')

    return render(request, "site/cards.html",{'form':form})

def usuarios(request):
    form = UsuariosForm
    if request.method == "POST":
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "site/usuarios.html",{'form':form})
