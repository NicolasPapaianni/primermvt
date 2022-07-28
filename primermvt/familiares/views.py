from tkinter.font import families
from django.http import HttpResponse
from django.shortcuts import render
from familiares.models import Familiares

def create_persona(request):
    create_persona = Familiares.objects.create(nombre = 'Paula Gonzalez', fecha_nacimiento = '1960-8-10' , edad = 62)
    context = {
        'create_persona' : create_persona
    }
    return render(request, 'create_persona.html', context = context)


def lista_familiares(request):
    familiares = Familiares.objects.all()
    context = {
        'familiares': familiares
    }
    return render(request, 'lista_familiares.html', context=context)
