from django.shortcuts import render
from django.contrib.auth.models import User
from main_app.models import Utilisateur, PharmacieDeGarde
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        username = Utilisateur.objects.get(user=request.user)
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
    return render(request, 'base.html', locals())

def premiersoins_view(request):
    if request.user.is_authenticated:
        username = Utilisateur.objects.get(user=request.user)
    title = 'Les Premiers Soins'
    return render(request, 'base.html', locals())