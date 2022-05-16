from django.shortcuts import render
from django.http import HttpResponse
from contacto.forms import Contacto
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def mensaje_contacto(request):

    if request.method=="POST":

        contacto_form = Contacto(request.POST)

        if contacto_form.is_valid():

            obtener_datos = contacto_form.cleaned_data
            return HttpResponse(str(obtener_datos))

    else:

        contacto_form = Contacto()

        return render (request, "contact_form.html", {"form": contacto_form})