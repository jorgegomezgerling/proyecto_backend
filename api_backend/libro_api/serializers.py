from rest_framework import serializers

from libro_api.models import Libro, User, Editorial, Autor

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'  # Incluye todos los campos de Editorial

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'  # Incluye todos los campos de Autor
