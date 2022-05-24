from django.shortcuts import render,redirect
from inventario.models import Productos
# Create your views here.


def compra(request,pk):
    producto= Productos.objects.get(id=pk)
    return render(request, 'domicilio.html', {'producto':producto})