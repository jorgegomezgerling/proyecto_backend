from django.db import models

# Create your models here.

class Editorial(models.Model):
    nombre = models.CharField(max_length=128)
    ciudad = models.CharField(max_length=128, default="Desconocida")

    def __str__(self):
        return f'{self.nombre} - {self.ciudad}'

class Libro(models.Model):
    titulo = models.CharField(max_length=128)
    cantidad_paginas = models.IntegerField()
    descatalogado = models.BooleanField(default=False)
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.titulo}'

class User(models.Model):
    nombre = models.CharField(max_length=128)
    libros = models.ManyToManyField(Libro, blank=True)

    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    libros = models.ManyToManyField(Libro, blank=True)

    def __str__(self):
        return f'{self.nombre}'
    
# Crear relaciones. Puede ser editorial y autor

