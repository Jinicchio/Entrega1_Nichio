from django.urls import path
from AppCoder.views import *

urlpatterns = [

    path('', inicio, name="inicio" ),
    path('ofertas/', ofertas, name="ofertas"),
    path('productos/', productos, name="productos"),
    path('sucursales/', sucursales, name="sucursales"),

    #Formularios
    path('ofertas_formulario/', ofertas_formulario, name="ofertas_formulario"),
    path('productos_formulario/', producto_formulario, name="productos_formulario"),
    path('sucursales_formulario/', sucursales_formulario, name="sucursales_formulario"),
    
    #Busqueda
    path('busquedaCamada/', busquedaCamada, name="busquedaCamada"),
    path('buscar/', buscar),
]