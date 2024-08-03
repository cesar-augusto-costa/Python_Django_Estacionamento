from django.shortcuts import render
from django.http import HttpResponse
from .models import Estacionamento

# Create your views here.


def home(request):
    return render(request, "estacionamento\home.html")


def listarEstacionamento(request):
    estacionamentos = Estacionamento.objects.all()  # busca todos os dados do banco
    return render(
        request,
        "estacionamento/listar_estacionamento.html",
        {"estacionamento": estacionamentos},
    )
