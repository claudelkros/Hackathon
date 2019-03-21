from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main_app.models import Utilisateur, Enew

@login_required(login_url="/login")
def index(request):
    if request.user.is_authenticated:
        username = Utilisateur.objects.get(user=request.user)
    return render(request, 'learning/index.html', locals())

def learningnews(request):
    if request.user.is_authenticated:
        username = Utilisateur.objects.get(user=request.user)
    enews = Enew.objects.all()
    return render(request, 'learning/learningNew.html', locals())