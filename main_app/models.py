from django.db import models
from django.contrib.auth.models import User
from _datetime import datetime, timedelta, tzinfo

# Create your models here.
class Utilisateur(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    centre_interet = models.CharField(max_length=200)
    numero = models.IntegerField(default=300)
    profil = models.CharField(max_length=300)
    def __str__(self):
        return self.user.username

