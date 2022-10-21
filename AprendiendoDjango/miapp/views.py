import http
from turtle import title
from django.shortcuts import render, HttpResponse,redirect
from miapp.models import Article, Category
from django.db.models import Q
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

def crear_articulo(request,title,content,public):
    articulo= Article(
        title=title,
        content=content,
        public=public
    )
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.title} - {articulo.content}")

def articulo(request):
    #articulo= Article.objects.get(pk=3)
    try:
        articulo= Article.objects.get(title="Tercer Articulo",public=True)
        response=f"Articulo: {articulo.title}"
    except:
        response="<h1>Articulo no encontrado</h1>"
    
    return HttpResponse(response)

def editar_articulo(request,id):
    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo Actualizado: {articulo.title} - {articulo.content}")

def articulos(request):
    
    articulos  = Article.objects.filter(title__contains="Articulo")
    articulos  = Article.objects.filter(title__exact="articulo",id__lte=2)
    articulos = Article.objects.all() #[2:3]
    articulos  = Article.objects.filter(id__gt=4)
    articulos  = Article.objects.filter(id__lt=4)
    articulos  = Article.objects.filter(id__gte=4)
    articulos = Article.objects.all()
    articulos = Article.objects.raw("select * from miapp_article where id=2")
    articulos = Article.objects.filter(
        Q(title__contains="2") | Q(title__contains="1")
    )
    return render(request,'articulos.html',{
        'articulos' : articulos
    })

def borrararticulo(request,id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos')

def save_article(request):
    articulo= Article(
        title=title,
        content=content,
        public=public
    )
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.title} - {articulo.content}")

def create_article(request):

    return render(request,'create_article.html')