from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from libro.models import Libro
from libro.serializer import LibroSerializer

# Create your views here.
class LibroView(ViewSet):
    def list(self, request):
        libro = Libro.objects.all()
        serializer = LibroSerializer(libro, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=422)

    def retrieve(self, request, pk=None):
        libro = get_object_or_404(Libro, pk=pk)
        serializer = LibroSerializer(libro)
        return Response(serializer.data)

    def update(self, request, pk=None):
        libro = get_object_or_404(Libro, pk=pk)
        serializer = LibroSerializer(libro, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        libro = get_object_or_404(Libro, pk=pk)
        try:
            libro.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_409_CONFLICT,
            data={
                'detail': str(e)
            })
