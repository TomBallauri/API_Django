from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE, IntegerField, DecimalField
from django.conf import settings

TYPE_MOTO = 'moto'
TYPE_AUTO = 'auto'
TYPE_CHOICES = [
    (TYPE_MOTO, 'Moto'),
    (TYPE_AUTO, 'Auto'),
]

# Create your models here.
class Product(Model):
    titre = CharField(max_length=512)
    type_vehicule = CharField(max_length=4, choices=TYPE_CHOICES)
    marque = CharField(max_length=64)
    image = CharField(max_length=256)
    chevaux = IntegerField()
    prix_ht = DecimalField(max_digits=12, decimal_places=2)
    contenu = TextField()
    auteur = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    date_creation = DateTimeField(auto_now_add=True)
    date_mise_a_jour = DateTimeField(auto_now=True)

class Comment(Model):
    contenu = TextField()
    auteur = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    date_creation = DateTimeField(auto_now_add=True)
    date_mise_a_jour = DateTimeField(auto_now=True)
    produit = ForeignKey(Product, on_delete=CASCADE, related_name='commentaires')

# Concessionnaire et Véhicule models
class Concessionnaire(Model):
    nom = CharField(max_length=64)
    siret = CharField(max_length=14)

class Vehicule(Model):
    type_vehicule = CharField(max_length=4, choices=TYPE_CHOICES)
    marque = CharField(max_length=64)
    image = CharField(max_length=256)
    chevaux = IntegerField()
    prix_ht = DecimalField(max_digits=12, decimal_places=2)
    concessionnaire = ForeignKey(Concessionnaire, on_delete=CASCADE, related_name='vehicules')
