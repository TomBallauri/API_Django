from django.db.models import Model, CharField, DateTimeField, ForeignKey, CASCADE, IntegerField, DecimalField, DateField
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

TYPE_MOTO = 'moto'
TYPE_AUTO = 'auto'
TYPE_CHOICES = [
    (TYPE_MOTO, 'Moto'),
    (TYPE_AUTO, 'Auto'),
]

# Concessionnaire et Véhicule models
class Concessionnaire(Model):
    nom = CharField(max_length=64)

    # Rajout d'un regex validator pour le siret pour s'assurer qu'il contient exactement 14 chiffres
    siret = CharField(
        max_length=14,
        validators=[
            RegexValidator(regex=r'^\d{14}$', message='Le SIRET doit contenir exactement 14 chiffres.')
        ],
    )


class Vehicule(Model):
    type = CharField(max_length=4, choices=TYPE_CHOICES)
    marque = CharField(max_length=64)
    image = CharField(max_length=256)
    chevaux = IntegerField()
    prix_ht = DecimalField(max_digits=12, decimal_places=2)

    #Colonne rajouter pour lier concessionnaire et vehicule
    concessionnaire = ForeignKey(Concessionnaire, on_delete=CASCADE, null=True, related_name='vehicules')


class AuthorUser(AbstractUser):
    date_of_birth = DateField(null=True, blank=True)
