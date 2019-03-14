from django.shortcuts import render
from main_app.models import Utilisateur
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    # if this is a POST request
    if request.method == 'POST':
        #Create a form instance and populate it with data from the request
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        verif_password = request.POST['verif_password']
        number = request.POST['number']
        centre_interet = request.POST['centre_interet']
        if password == verif_password:
            utilisateur = Utilisateur()
            utilisateur.centre_interet = centre_interet
            utilisateur.numero = number
            user = User()
            user.username = username
            user.email = email
            user.password = password
            utilisateur.user = user
            user.save()
            utilisateur.save()
            return render(request, 'main/home.html')
    else:
        form = Utilisateur()
    return render(request, 'main/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'main/home.html')

def home(request):
    if request.user.is_authenticated:
        username = Utilisateur.objects.get(user=request.user)
        print(username)
        return render(request, 'main/home.html', locals())
    else:
        print('none')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return render(request, 'main/home.html')
        else:
            return render(request, 'main/login.html')
    return render(request, 'main/login.html')

def sante(request):
    pass