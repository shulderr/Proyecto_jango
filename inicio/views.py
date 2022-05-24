from django.shortcuts import render
from django.http import HttpResponse
from inventario.models import Productos
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):

    productos = Productos.objects.all()
    return render(request, 'inicio.html', {'productos':productos})
