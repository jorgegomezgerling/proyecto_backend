from django import forms

from libro_api.models import Libro, Autor, Editorial

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            'titulo',
            'cantidad_paginas',
            'descatalogado',
            'editorial',
        ]

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = [
            'nombre',
            'apellido',
            'libros',
        ]

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = [
            'nombre',
            'ciudad',
        ]
