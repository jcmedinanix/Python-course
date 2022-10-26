from email.policy import default
from tabnanny import verbose
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150,verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null',verbose_name="Miniatura")
    public = models.BooleanField(verbose_name="Publicado?")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Actualizado")

    class Meta:
        verbose_name="Articulo"
        verbose_name_plural="Articulos"
        ordering=['-id']

    def __str__(self):

        if self.public:
            public="(Publicado)"
        else:
            public="(Privado)"

        return f"{self.title} {public}"   
        #return f"{self.title} creado el {self.created_at} ({self.public})"


class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
