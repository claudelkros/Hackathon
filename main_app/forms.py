from django import forms

from django import forms

class Utilisateur(forms.Form):
    first_name = forms.CharField(label='Nom', max_length=100)
    first_name.widget.attrs.update({'class': 'form-control offset-md-3'})
    first_name.widget.attrs.update({'placeholder': 'Entrez votre Nom'})

    last_name = forms.CharField(label='Prenom', max_length=100)
    last_name.widget.attrs.update({'class': 'form-control offset-md-3'})
    last_name.widget.attrs.update({'placeholder': 'Entrez votre Prenom'})

    email = forms.CharField(label='Email', max_length=100)
    email.widget.attrs.update({'class': 'form-control offset-md-3'})
    email.widget.attrs.update({'placeholder': 'Entrez votre email'})

    password = forms.CharField(label='Password', max_length=100)
    password.widget.attrs.update({'class': 'form-control offset-md-3'})
    password.widget.attrs.update({'placeholder': 'Entrez votre Mot de passe'})

    numero = forms.CharField(label='Numero', max_length=100)
    numero.widget.attrs.update({'class': 'form-control offset-md-3'})
    numero.widget.attrs.update({'placeholder': 'Enter the city in which you want to live 🔑'})

    centre_interet = forms.CharField(label='Centre d\'interêt', max_length=100)
    centre_interet.widget.attrs.update({'class': 'form-control offset-md-3'})
    centre_interet.widget.attrs.update({'placeholder': 'Enter the city in which you want to live 🔑'})