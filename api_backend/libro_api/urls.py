from django.urls import path
from libro_api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('libros_rest/', views.libros_rest, name='libros_rest')
]