from . import views
from django.urls import path
app_name = 'main_app'

urlpatterns = [
	path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
	path('logout', views.logout_view, name='logout'),
    path('home',  views.home, name='home')
]
