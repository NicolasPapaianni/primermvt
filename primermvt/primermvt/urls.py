
from django.contrib import admin
from django.urls import path
from primermvt.views  import saludo, template
from familiares.views import create_persona, lista_familiares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name = 'saludo'),
    path('template/', template, name = 'template'),
    path('create_persona/', create_persona, name = 'create_persona'),
    path('lista_familiares/', lista_familiares, name = 'lista_familiares')
]
