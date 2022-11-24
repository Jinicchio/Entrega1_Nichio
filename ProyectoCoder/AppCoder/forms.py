from django import forms

class Sucursales_formulario(forms.Form):

    direccion = forms.CharField(max_length=40)
    telefono = forms.IntegerField()

class Productos_formulario(forms.Form):

    descripcion_del_producto = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=50)
    precio= forms.IntegerField()

class Oferta_formulario(forms.Form):

    descripcion_del_producto = forms.CharField(max_length=100)
    marca = forms.CharField(max_length=50)
    precio = forms.IntegerField()
    descuento = forms.CharField(max_length=50)