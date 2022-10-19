import http
from django.shortcuts import render, HttpResponse,redirect
#Menu
template = """

"""

# Create your views here.
def hola_mundo(request,redirigir=0):
    if redirigir == 1:
       return redirect('/contacto/hola/apellidos')
    
    #return HttpResponse(template + "Hello world")
    return render(request,"hola_mundo.html")

def index(request):
    return render(request,"index.html")
  ###  return HttpResponse(template + """
  ##  <H1> PAGINA PRINCIPAL</H1>
  ##  """)

def bucle_while(request):
    anio = 2022
    var_html = [] 

    while(anio < 2051):
        if anio % 2 == 0:
            var_html.append(anio)
            
        anio += 1

        ##return HttpResponse(template + html)
    return render(request,'bucle_while.html', {
        'var_bucle': 'Años hasta el 2050',
        'var_html' : var_html,
    })

def contacto(request,nombre="Juan",apellidos="Medina"):
    return HttpResponse(template + f"<h2>Contacto:{nombre} {apellidos}</h2>")