from django.shortcuts import render
from libro_api.models import Libro
from libro_api.serializers import LibroSerializer
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

def index(request):
    libros = Libro.objects.all().order_by('titulo')
    for libro in libros:
        autores = libro.autor_set.all()  # Obtener todos los autores del libro
        print(f'Libro: {libro}, Autores: {autores}')
    return render(request, 'index.html', {'libros': libros})

def get_all_libros():
    libros = Libro.objects.all().order_by('titulo')
    libros_serializers = LibroSerializer(libros, many=True)
    return libros_serializers.data

def libros_rest(request):
    libros = get_all_libros()
    return JsonResponse(libros, safe=False)