from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def task_list(request):
    return HttpResponse("Hello World !")


def task_create(request):
    return HttpResponse("Création d'une tâche")


def task_details(request, id):
    return HttpResponse(f"Détails d'une tâche : {id}")


def task_update(request, id):
    return HttpResponse(f"update d'une tâche : {id}")


def task_delete(request, id):
    return HttpResponse(f"Suppression d'une tâche : {id}")
