from django.db import models
from django.contrib.auth.models import User
from _datetime import datetime, timedelta, tzinfo

# Create your models here.
#declaration du modèle
#enumeration des attributs du modèle
#__str__ permet de nommer notre classe dans le dashboard admin
class Utilisateur(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    centre_interet = models.CharField(max_length=200)
    numero = models.IntegerField(default=300)
    profil = models.CharField(max_length=300)
    def __str__(self):
        return self.user.username

class Carnet(models.Model):
    numeroCarnet = models.CharField(max_length=12)
    nomPatient = models.CharField(max_length=200)
    alergie = models.CharField(max_length=200)
    age = models.IntegerField(default=100)
    numberEmergency = models.IntegerField(default=100)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    consultation = models.ForeignKey('Consultation', on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Consultation(models.Model):
    date = models.DateTimeField(default=timedelta)
    traitement = models.CharField(max_length=500)
    observation = models.CharField(max_length=500)
    analyse = models.CharField(max_length=400)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.traitement

class MedecineNaturelle(models.Model):
    titre = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/", default="", blank=True, null=True)
    contenu = models.TextField(max_length=500)
    date_pubication = models.DateTimeField(null=True, blank=True)
    feedback_sante = models.IntegerField(default=100)

    def __str__(self):
        return self.titre

class Maladie(models.Model):
    nommaladie = models.CharField(max_length=100)
    symtome = models.CharField(max_length=100)

    def __str__(self):
        return self.nommaladie

class Memoire (models.Model):
    theme = models.CharField(max_length=100)
    filiere = models.CharField(max_length=100)
    annee = models.CharField(max_length=15)
    niveau = models.IntegerField(default=15)
    redacteur = models.CharField(max_length=300)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.theme

class Produit (models.Model):
    nomproduit = models.CharField(max_length=100)
    prix = models.CharField(max_length=50)
    numvendeur = models.IntegerField(default=15)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nomproduit


class Culture(models.Model):
    nomculture = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    guide = models.CharField(max_length=15)

    def __str__(self):
        return self.nomculture


