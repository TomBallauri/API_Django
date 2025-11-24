from django.contrib.auth.models import AbstractUser
from django.db.models import DateField


class AuthorUser(AbstractUser):
    date_of_birth: DateField(null=False, blank=True)