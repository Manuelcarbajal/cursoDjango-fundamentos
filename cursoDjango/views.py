from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render

#Request: Para realiazr petisones 
#HttpResponse : para enviar respuestas usando el protoclo http

#Esto es una vista:
def welcome(request):#pasamos un objecto de tipo request como primer argumento
    return HttpResponse("Hola MOMI")

def welcomeRed(request):#pasamos un objecto de tipo request como primer argumento
    return HttpResponse("<p style='color: red' >Hola MOMI </p>")


def categoriaEdad(request,edad):
    if edad >= 18:
        if edad >= 60:
            categoria = 'tercer edad'
        else:
            categoria = 'adultez'
    else:
        if edad <= 10:
            categoria = 'Infancia'
        else:
            categoria = 'Adolesecnia'
    
    resultado = '<h1>Categoria de la edad: %s</h1>' %categoria
    return HttpResponse(resultado)


def optenmoment(request):
    respuerta = '<h1>Momento actual: {0}</h1>'.format(datetime.datetime.now().strftime('%A %d/ %m/ %y %H:%M:%S'))
    
    return HttpResponse(respuerta)



def contenidohtml(request,name,age):
    contenido = """
    <html>
        <body>
            <p>
                Name:%s / age: %s
            </p>
        </body>
    </html>

    """ % (name,age)
    return HttpResponse(contenido)


def myplantillaone(request):
    #abrimos el documento que contine a la plantilla
    plantillaExterna = open("C:/Users/manue/Documents/Programacion/proyectos django/cursoDjango/cursoDjango/plantillas/plantillaHtml-one.html")
    #caragar el docuemnto en una variable de tipo template
    template = Template(plantillaExterna.read())

    #cerrar docuemntoe xterno que hemos abierto
    plantillaExterna.close()
    #crear un contexto
    contexto = Context()
    #rederizar el documento 
    document = template.render(contexto)
    return HttpResponse(document)


def plantillaParametros(request):
    nombre = "DominikoXd" #usar comilla dobles para que sea valido
    fecha = datetime.datetime.now()
    lenguajes = ["Python","Jsx","js","Java","Ruby","C#"]
    #abrimos el documento que contine a la plantilla
    plantillaExterna = open("C:/Users/manue/Documents/Programacion/proyectos django/cursoDjango/cursoDjango/plantillas/plantillaHtml-one.html")
    #caragar el docuemnto en una variable de tipo template
    template = Template(plantillaExterna.read())

    #cerrar docuemntoe xterno que hemos abierto
    plantillaExterna.close()
    #crear un contexto
    contexto = Context({"nombreCanal": nombre, "Fecha" : fecha , "lenguajes" : lenguajes})
    #rederizar el documento 
    document = template.render(contexto)
    return HttpResponse(document)


def plantillaCargador(request):
    nombre = "DominikoXd" #usar comilla dobles para que sea valido
    fecha = datetime.datetime.now()
    lenguajes = ["Python","Jsx","js","PHP","Java","Ruby","C#"]
    #Especificamos la carpeta donde se encutran la splantillas y creamos una variable que las alamcena en stetting template dirs
    plantillasExternas = get_template.get_template('plantillaHtml-one.html')
    #rederizar docuemnto que se va retornar
    document = plantillasExternas.render({"nombreCanal": nombre, "Fecha" : fecha , "lenguajes" : lenguajes})
    return HttpResponse(document)


def plantillashortCut(request):
    nombre = "DominikoXd" #usar comilla dobles para que sea valido
    fecha = datetime.datetime.now()
    lenguajes = ["Python","Jsx","js","PHP","Java","C++","Ruby","C#"]

    return render(request,'plantillaHtml-one.html',{"nombreCanal": nombre, "Fecha" : fecha , "lenguajes" : lenguajes})


def plantillahija1(request):
    return render(request,"plantillahija1.html",{})

def plantillahija2(request):
    return render(request,"plantillahija2.html",{})