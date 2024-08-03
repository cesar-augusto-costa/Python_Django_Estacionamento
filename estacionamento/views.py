from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "estacionamento\home.html")


def listarEstacionamento(request):
    tarefas = [{"id": "1", "Tarefa": "comprar fraldas"}]
    return render(
        request, "estacionamento/listar_estacionamento.html", {"tarefas": tarefas}
    )
