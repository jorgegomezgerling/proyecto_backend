from django.urls import path
from libro_api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('libros_rest/', views.libros_rest, name='libros_rest'),
    path('autores_rest/', views.autores_rest, name='autores_rest'),
    path('editoriales_rest/', views.editoriales_rest, name='editoriales_rest'),
    #path('add_libro/', views.add_libro_view, name='add_libro_rest'),
]

