from django.shortcuts import render, get_object_or_404
from django.db.models.deletion import ProtectedError

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from autor.models import Autor
from autor.serializer import AutorSerializer
# Create your views here.
class AutorView(ViewSet):
    def list(self, request):
        autor = Autor.objects.all()
        serializer = AutorSerializer(autor, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=422)

    def retrieve(self, request, pk=None):
        autor = get_object_or_404(Autor, pk=pk)
        serializer = AutorSerializer(autor)
        return Response(serializer.data)

    def update(self, request, pk=None):
        autor = get_object_or_404(Autor, pk=pk)
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        autor = get_object_or_404(Autor, pk=pk)
        try:
            autor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            return Response(status=status.HTTP_409_CONFLICT,
            data={
                'detail': 'Este autor no se puede eliminar porque tiene libros asociados.'
            })

