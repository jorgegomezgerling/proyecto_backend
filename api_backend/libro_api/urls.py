from django.urls import path
from libro_api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]