from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse('<h1>view Home</h1>')
    return render(request, "estacionamento\home.html")


def listarEstacionamento(request):
    return render(request, "estacionamento/listar_estacionamento.html")
