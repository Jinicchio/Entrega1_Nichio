from django.http import HttpResponse
from AppCoder.models import Sucursales, Productos, Ofertas
from django.shortcuts import render 
from AppCoder.forms import Sucursales_formulario , Oferta_formulario, Productos_formulario



# Create your views here.

def inicio(request):
    return render(request, "AppCoder/padre.html")

def ofertas(request):
    return render(request, "AppCoder/ofertas.html")

def productos(request):
    return render(request, "AppCoder/productos.html")

def sucursales(request):
    return render(request, "AppCoder/sucursales.html")

# Create your forms here.
def ofertas_formulario(request):

    if request.method == "POST":
        
        miformulario = Oferta_formulario(request.POST)
        
        # Validamos que el formulario no tenga problemas
        if miformulario.is_valid():
            #recuperamos los datos del atributo cleaned_data
            data = miformulario.cleaned_data

            ofertas = Ofertas(descripcion_del_producto=data["descripcion_del_producto"],marca=data["marca"],precio=data["precio"],descuento=data["descuento"])
            
            ofertas.save()
    
    miformulario = Oferta_formulario()
    
    contexto= {"miformulario": miformulario}
    
    return render(request,"AppCoder/ofertas_formulario.html", contexto)

def producto_formulario(request):
    
    if request.method == "POST":
        
        miformulario = Productos_formulario(request.POST)
        # Validamos que el formulario no tenga problemas
        if miformulario.is_valid():
            #recuperamos los datos del atributo cleaned_data
            data = miformulario.cleaned_data

            productos = Productos(descripcion_del_producto=data["descripcion_del_producto"],marca=data["marca"],precio=data["precio"])
            
            productos.save()
    
    miformulario = Productos_formulario()
    
    contexto= {"miformulario": miformulario}
    
    return render(request,"AppCoder/productos_formulario.html", contexto)


def sucursales_formulario(request):
    
    if request.method == "POST":
        
        miformulario = Sucursales_formulario(request.POST)
        # Validamos que el formulario no tenga problemas
        if miformulario.is_valid():
            #recuperamos los datos del atributo cleaned_data
            data = miformulario.cleaned_data

            sucursales = Sucursales(direccion=data["direccion"],telefono=data["telefono"])
            
            sucursales.save()
    
    miformulario = Sucursales_formulario()
    
    contexto= {"miformulario": miformulario}
    
    return render(request,"AppCoder/sucursales_formulario.html", contexto)

def busquedaCamada(request):

    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    if request.GET['nombre_producto']:
        
        #respuesta= f"Estoy buscando el producto: {request.GET['nombre_producto']}"
        
        nombre_producto=request.GET['nombre_producto']
        
        producto= Productos.objects.filter(descripcion_del_producto__icontains=nombre_producto)
        
        return render(request, "AppCoder/resultadosBusqueda.html", {"producto":producto, "nombre_producto":nombre_producto})
    
    else:
        
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)