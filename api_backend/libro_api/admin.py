from django.contrib import admin
from libro_api.models import Libro, User

# Register your models here.

admin.site.register(Libro)
admin.site.register(User)