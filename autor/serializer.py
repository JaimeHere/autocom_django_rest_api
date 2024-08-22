
from rest_framework import serializers
from autor.models import Autor
from libro.models import Libro
from libro.serializer import LibroSerializer

class AutorSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(max_length=100)
    apellido = serializers.CharField(max_length=100)
    libros_publicados = serializers.SerializerMethodField()
    
    class Meta:
        model = Autor
        fields = '__all__'
    
    def get_libros_publicados(self, obj):
        return Libro.objects.all().filter(autor_id=obj.id).count()