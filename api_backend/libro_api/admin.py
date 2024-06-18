from django.contrib import admin
from libro_api.models import Libro, User, Autor, Editorial

# Register your models here.

admin.site.register(Libro)
admin.site.register(User)
admin.site.register(Autor)
admin.site.register(Editorial)