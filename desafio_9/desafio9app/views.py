from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Bienvenido a mi sitio web!")


# Create your views here.
