from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=128)
    autor = models.CharField(max_length=128)
    cantidad_paginas = models.IntegerField()
    editorial = models.CharField(max_length=128)
    descatalogado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.titulo} - {self.autor}'


class User(models.Model):
    nombre = models.CharField(max_length=128)
    libros = models.ManyToManyField(Libro, blank=True)

    def __str__(self):
        return self.nombre