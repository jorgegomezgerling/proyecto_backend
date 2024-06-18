from rest_framework import serializers

from libro_api.models import Libro, User

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'