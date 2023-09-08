from rest_framework import serializers
from .models import Denuncia, Demandado


class DenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denuncia
        fields = '__all__'


class DemandadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demandado
        fields = '__all__'
