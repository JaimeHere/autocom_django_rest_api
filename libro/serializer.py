
from rest_framework import serializers
from .models import Libro

class LibroSerializer(serializers.ModelSerializer):
    titulo = serializers.CharField(max_length=100)

    autor_name = serializers.SerializerMethodField()

    class Meta:
        model = Libro
        fields = '__all__'
    
    def get_autor_name(self, obj):
        return '{} {}'.format(obj.autor.nombre, obj.autor.apellido)