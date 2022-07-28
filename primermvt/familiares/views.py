from tkinter.font import families
from django.http import HttpResponse
from django.shortcuts import render
from familiares.models import Familiares

# Create your views here.

def create_persona(request):
    nueva_persona = Familiares.objects.create(nombre = 'Paula Gonzalez', fecha_nacimiento = '1960-8-10' , edad = 62)
    context = {
        'nueva_persona' : nueva_persona
    }
    return render(request, 'nueva_persona.html', context = context)


def lista_familiares(request):
    familiares = Familiares.objects.all()
    context = {
        'familiares': familiares
    }
    return render(request, 'lista_familiares.html', context=context)
