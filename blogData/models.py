from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE, IntegerField, DecimalField
from django.core.validators import RegexValidator
from apiBlog import settings


# Concessionnaire et Véhicule models
class Concessionnaire(Model):
    nom = CharField(max_length=64)
    siret = CharField(max_length=14)

class Vehicule(Model):
    TYPE_MOTO = 'moto'
    TYPE_AUTO = 'auto'
    TYPE_CHOICES = [
        (TYPE_MOTO),
        (TYPE_AUTO),
    ]

    type = CharField(max_length=4, choices=TYPE_CHOICES)
    marque = CharField(max_length=64)
    chevaux = IntegerField()
    prix_ht = DecimalField(max_digits=12, decimal_places=2)
    concessionnaire = ForeignKey(Concessionnaire, on_delete=CASCADE, related_name='vehicules')