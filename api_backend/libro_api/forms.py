from django import forms

from libro_api.models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            'titulo',
            'cantidad_paginas',
            'descatalogado',
            'editorial',
        ]