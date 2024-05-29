from django.urls import path
from libro_api import views

urlpatterns = [
    path('', views.index, name='index'),
]