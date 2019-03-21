from django.shortcuts import render
from main_app.models import Utilisateur, MedecineNaturelle
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('main_app:home')
    else:
        title = "Index"
        return render(request, 'main/home.html', locals())

def register(request):
    error = False
    if request.user.is_authenticated:
        return redirect('main_app:home')
    else:
        # if this is a POST request
        if request.method == 'POST':
            #Create a form instance and populate it with data from the request
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            verif_password = request.POST['verif_password']
            number = request.POST['number']
            centre_interet = request.POST['centre_interet']
            profil = request.POST['profil']
            if password == verif_password:
                utilisateur = Utilisateur()
                utilisateur.centre_interet = centre_interet
                utilisateur.numero = number
                utilisateur.profil = profil
                user = User()
                user.username = username
                user.email = email
                user.password = password
                utilisateur.user = user
                try:
                    user.save()
                    utilisateur.save()
                except:
                    error = True
                return redirect('main_app:home')
        else:
            form = Utilisateur()
            title = 'Enreigistrement'
    return render(request, 'main/register.html', locals())

def logout_view(request):
    logout(request)
    return redirect('main_app:index')

def home(request):

    if request.user.is_authenticated:
        username = Utilisateur.objects.get(user=request.user)
        title = 'Accueil'
        return render(request, 'main/home.html', locals())
    else:
        return redirect('main_app:login')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('main_app:home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('main_app:home')
            else:
                return redirect('main_app:login')
        title = 'Login'
    return render(request, 'main/login.html', locals())

def profil_view(request):
    username = Utilisateur.objects.get(user=request.user)
    return render(request, 'main/profil.html', locals())