from rest_framework.serializers import ModelSerializer
from .models import Concessionnaire, Vehicule, AuthorUser


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


class AuthorUserSerializer(ModelSerializer):
    class Meta:
        model = AuthorUser
        fields = [
            'id',
            'username',
            'password',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = AuthorUser(**validated_data)
        user.set_password(password)
        user.save()
        return user