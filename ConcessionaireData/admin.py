from django.contrib import admin

from ConcessionaireData.models import Concessionnaire, Vehicule, AuthorUser

# Register your models here.
admin.site.register(Concessionnaire)
admin.site.register(Vehicule)
admin.site.register(AuthorUser)