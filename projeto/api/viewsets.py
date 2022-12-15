from rest_framework import viewsets
from projeto.api import serializers
from autor.models import Autor
from coorientador.models import Coorientador
from monografia.models import Monografia
from orientador.models import Orientador

class AutorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AutorSerializer
    queryset = Autor.objects.all()

class OrientadorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrientadorSerializer
    queryset = Orientador.objects.all()

class CoorientadorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CoorientadorSerializer
    queryset = Coorientador.objects.all()

class MonografiaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MonografiaSerializer
    queryset = Monografia.objects.all()