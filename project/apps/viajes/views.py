from django.shortcuts import render

# Create your views here.
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render






def salta(request: HttpRequest) -> HttpResponse:
    return render(request, "viajes/salta.html")

def jujuy(request: HttpRequest) -> HttpResponse:
    return render(request, "viajes/jujuy.html")

def mendoza(request: HttpRequest) -> HttpResponse:
    return render(request, "viajes/mendoza.html")

def cataratas(request: HttpRequest) -> HttpResponse:
    return render(request, "viajes/cataratas.html")

def perito(request: HttpRequest) -> HttpResponse:
    return render(request, "viajes/perito.html")

def rioja(request: HttpRequest) -> HttpResponse:
    return render(request, "viajes/rioja.html")

def bariloche(request: HttpRequest) -> HttpResponse:
    return render(request, "viajes/bariloche.html")

def santarosa(request: HttpRequest) -> HttpResponse:
    return render(request, "viajes/santarosa.html")



