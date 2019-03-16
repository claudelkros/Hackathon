from django.shortcuts import render
from main_app.models import *
#

def index(request):
        all_news = New.objects.all()
        return render(request, 'enews/index.html', locals())

def lecture_view(request, id):
        new = New.objects.get(id=id)
        return render(request, 'enews/single.html', locals())