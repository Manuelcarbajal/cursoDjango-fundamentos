
from django.contrib import admin
from django.urls import path
from cursoDjango.views import welcome,welcomeRed
from cursoDjango.views import categoriaEdad
from cursoDjango.views import optenmoment,contenidohtml
from cursoDjango.views import myplantillaone,plantillaParametros
from cursoDjango.views import plantillaCargador,plantillashortCut
from cursoDjango.views import plantillahija1,plantillahija2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome),
    path('welcomered/',welcomeRed),
    path('CaEdad/<int:edad>/',categoriaEdad),
    path('date/', optenmoment),
    path('contentHtml/<name>/<int:age>/',contenidohtml),
    path('plantillaOne/',myplantillaone),
    path('plantillaParametros/',plantillaParametros),
    path('plantillasCargador/',plantillaCargador),
    path('plantillashortCut/',plantillashortCut),
    path('plantillahija1/',plantillahija1),
    path('plantillahija2/',plantillahija2)
]
