from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return HttpResponse("<h1>Hola Mundo</h1>")
def bienvenido(request):
    return render(request, 'paginas/bienvenido.html')