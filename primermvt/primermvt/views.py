from django.http import HttpResponse
from django.shortcuts import render            # para crear el template
from datetime import datetime


def saludo(request):
    return HttpResponse('Buen dia Coderhouse, les presento a mi familia')


def  template(request):
    today = datetime.now().date
    context = {'lista': ['Nicolas Papaianni', 'Martin Papaianni', 'Carlos Papaianni', 'Paula Gonzalez'],

        'today' : today
    }
    return render(request, 'template.html', context = context)



