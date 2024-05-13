from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    return render(request,'index.html')

def variavel(request):
    x = "teste com alunos"
    [1,2,3,4,5]
    return render(request,'index.html',{"index" : x, "y" : [1,2,3,4,5]})