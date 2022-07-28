from tkinter.font import families
from django.http import HttpResponse
from django.shortcuts import render
from familiares.models import Familiares

def create_persona(request):
    # create_persona = Familiares.objects.create(nombre = 'Nicolas Papaianni', fecha_nacimiento = '1988-07-10' , edad = 34)
    # create_persona = Familiares.objects.create(nombre = 'Martin Papaianni', fecha_nacimiento = '1990-09-10' , edad = 32)
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
