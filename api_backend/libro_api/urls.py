from django.urls import path
from libro_api import views

urlpatterns = [
    path('index_libros', views.index, name='index_libros'),
    path('libros_rest/', views.libros_rest, name='libros_rest'),
    path('autores_rest/', views.autores_rest, name='autores_rest'),
    path('editoriales_rest/', views.editoriales_rest, name='editoriales_rest'),
    path('nuevo_libro/', views.NewLibroView.as_view(), name='nuevo_libro'),
    path('nuevo_autor/', views.NewAutorView.as_view(), name='nuevo_autor'),
    path('nueva_editorial/', views.NewEditorialView.as_view(), name='nueva_editorial'),
]

