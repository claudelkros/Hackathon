from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main_app.models import Utilisateur, PharmacieDeGarde, MedecineNaturelle, Premiersoins, Dicomedical
# Create your views here.

@login_required(login_url="/login")
def index(request):
    if request.user.is_authenticated:
        username = Utilisateur.objects.get(user=request.user)
        title = 'Health Services'
        return render(request, 'health_services/index.html', locals())

def pharmacie_view(request):
    if request.user.is_authenticated:
        username = Utilisateur.objects.get(user=request.user)
    title = 'Pharmacie de Garde'
    pharmacie_all = PharmacieDeGarde.objects.all()
    return render(request, 'health_services/pharmacie.html', locals())

def medecinenaturel_view(request):
    if request.user.is_authenticated:
        username = Utilisateur.objects.get(user=request.user)
    title = 'Medécine Naturelle'
    medecines = MedecineNaturelle.objects.all()
    return render(request, 'health_services/medecinetraditionnel.html', locals())

def premiersoins_view(request):
    if request.user.is_authenticated:
        username = Utilisateur.objects.get(user=request.user)
    title = 'Les Premiers Soins'
    premiersoins = Premiersoins.objects.all()
    return render(request, 'health_services/premiersoins.html', locals())

def dicomedical_view(request):
    if request.user.is_authenticated:
        username = Utilisateur.objects.get(user=request.user)
    title = 'Le Dictionnaire Medical'
    dicomedicals = Dicomedical.objects.all()
    return render(request, 'health_services/dicomedical.html', locals())