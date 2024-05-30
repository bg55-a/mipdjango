from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def profile(request):
    return render(request, 'account/profile.html')

def inicio(request):
    return render(request, 'core/inicio.html')
def compartir(request):
    return render(request, 'core/compartir.html')
def diagnostico(request):
    return render(request, 'core/diagnostico.html')
def ejecucion(request):
    return render(request, 'core/ejecucion.html')
def entendimiento(request):
    return render(request, 'core/entendimiento.html')
def planeacion(request):
    return render(request, 'core/planeacion.html')
def geomorfo(request):
    return render(request, 'core/mapas/geomorfo.html')
def socioeconomicos(request):
    return render(request, 'core/mapas/socioeconomicos.html')

def index(request):
    return render(request, 'core/index.html')

