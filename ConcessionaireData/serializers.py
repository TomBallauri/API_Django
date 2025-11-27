from rest_framework.serializers import ModelSerializer
from .models import Concessionnaire, Vehicule


class VehiculeSerializer(ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'

class ConcessionnaireSerializer(ModelSerializer):

    class Meta:
        model = Concessionnaire
        fields = ['id', 'nom']

class ConcessionnaireCreateSerializer(ModelSerializer):
    class Meta:
        model = Concessionnaire
        fields = ['id', 'nom', 'siret']