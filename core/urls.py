from django.urls import path
from .views import home, profile, inicio, compartir, diagnostico, ejecucion,entendimiento, planeacion, geomorfo, socioeconomicos, index

urlpatterns = [
    path('', home, name='home'),
    path('accounts/profile/', profile, name='profile'),
    path('inicio', inicio, name='inicio'),
    path('compartir', compartir, name='compartir'),
    path('diagnostico', diagnostico, name='diagnostico'),
    path('ejecucion', ejecucion, name='ejecucion'),
    path('entendimiento', entendimiento, name='entendimiento'),
    path('planeacion', planeacion, name='planeacion'),
    path('geomorfo', geomorfo, name='geomorfo'),
    path('socioeconomicos', socioeconomicos, name='socioeconomicos'),
    path('index', index, name='index'),
]