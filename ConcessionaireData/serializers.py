from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField, DateTimeField
from .models import Product, Comment, Concessionnaire, Vehicule


class ProductListSerializer(ModelSerializer):
    auteur = StringRelatedField(read_only=True)
    date_creation = DateTimeField(read_only=True)
    date_mise_a_jour = DateTimeField(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'titre', 'auteur', 'date_creation', 'date_mise_a_jour']


class ProductDetailSerializer(ModelSerializer):
    auteur = StringRelatedField(read_only=True)
    date_creation = DateTimeField(read_only=True)
    date_mise_a_jour = DateTimeField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    # Les champs en lecture seule car ils sont gérés automatiquement
    auteur = StringRelatedField(read_only=True)
    produit = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class VehiculeSerializer(ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'


class ConcessionnaireSerializer(ModelSerializer):
    # Expose tous les champs sauf `siret` (doit rester en base mais non accessible via l'API)
    class Meta:
        model = Concessionnaire
        fields = ['id', 'nom']