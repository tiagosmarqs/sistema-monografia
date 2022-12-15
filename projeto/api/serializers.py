from rest_framework import serializers
from autor.models import Autor
from coorientador.models import Coorientador
from monografia.models import Monografia
from orientador.models import Orientador

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class OrientadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orientador
        fields = '__all__'

class CoorientadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coorientador
        fields = '__all__'

class MonografiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monografia
        fields = '__all__'