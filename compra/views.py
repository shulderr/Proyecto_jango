from django.shortcuts import render,redirect
from inventario.models import Productos
from compra.models import pedidos
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import time
from django.contrib.auth.decorators import login_required

# Create your views here.


def Enviar_correo(email, nombre, producto, precio, ciudad):

    fecha = str(time.strftime("%d/%m/%Y"))
    context = {'email':email, 'nombre':nombre, 'producto':producto, 'precio':precio, 'ciudad':ciudad, 'fecha':fecha}
    template = get_template('correo.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        'Un Correo De Prueba',
        'Geralt',
        settings.EMAIL_HOST_USER,
        [email]
    )

    mail.attach_alternative(content, 'text/html')
    try:
        mail.send()
    except:
        print("Error al Enviar el correo")


def Enviar_correo_admin(nombre, producto, precio, ciudad):

    email = 'shulder2@gmail.com'
    fecha = str(time.strftime("%d/%m/%Y"))
    context = {'email':email, 'nombre':nombre, 'producto':producto, 'precio':precio, 'ciudad':ciudad, 'fecha':fecha}
    template = get_template('correo_admin.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        'Pedido en Sp-indumentary',
        'Geralt',
        settings.EMAIL_HOST_USER,
        [email]
    )

    mail.attach_alternative(content, 'text/html')
    try:
        mail.send()
    except:
        print("Error al Enviar el correo")


def compra(request,pk):

    producto = Productos.objects.get(id=pk)
    return render(request, "domicilio.html", {'producto': producto})


def venta(request):

    if request.method == "POST":

        nombre = request.POST["nombre"]
        documento = request.POST["cedula"]
        correo = request.POST["correo"]
        direccion = request.POST["direccion"]
        departamento = request.POST["departamento"]
        ciudad = request.POST["ciudad"]
        telefono = request.POST["tel"]
        producto = request.POST["producto"]
        precio = request.POST["precio"]
        Enviar_correo(correo, nombre, producto, precio, ciudad)
        Enviar_correo_admin(nombre, producto, precio, ciudad)
        data = pedidos(nombre=nombre, documento=documento, correo=correo, direccion=direccion,
                       departamento=departamento,
                       ciudad=ciudad, telefono=telefono)
        data.save()

        return redirect('home')