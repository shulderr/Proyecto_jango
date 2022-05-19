from django.shortcuts import render

# Create your views here.


def compra(request):
    return render(request, 'domicilio.html')