from django.shortcuts import render
from libro_api.models import Libro, Autor, Editorial
from libro_api.serializers import LibroSerializer, EditorialSerializer, AutorSerializer
from django.http import JsonResponse
from libro_api.forms import LibroForm

def index(request):
    libros = Libro.objects.all().order_by('titulo')
    editoriales = Editorial.objects.all().order_by('nombre')
    autores = Autor.objects.all().order_by('apellido')
    
    for libro in libros:
        autores_libro = libro.autor_set.all() 
        print(f'Libro: {libro}, Autores: {autores_libro}')

    context = {
        'libros': libros,
        'editoriales': editoriales,
        'autores': autores
    }
    return render(request, 'index.html', context)


# PARA LIBROS
def get_all_libros():
    libros = Libro.objects.all().order_by('titulo')
    libros_serializers = LibroSerializer(libros, many=True)
    return libros_serializers.data

def libros_rest(request):
    libros = get_all_libros()
    return JsonResponse(libros, safe=False)


# PARA AUTORES
def get_all_autores():
    autores = Autor.objects.all()
    autores_serializers = AutorSerializer(autores, many=True)
    return autores_serializers.data

def autores_rest(request):
    autores = get_all_autores()
    return JsonResponse(autores, safe=False)


#PARA EDITORIALES

def get_all_editorial():
    editoriales = Editorial.objects.all().order_by('nombre')
    editoriales_serializers = EditorialSerializer(editoriales, many=True)
    return editoriales_serializers.data

def editoriales_rest(request):
    editoriales = get_all_editorial()
    return JsonResponse(editoriales, safe=False)

#PARA FORMULARIOS


