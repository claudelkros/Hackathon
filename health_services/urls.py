from . import views
from django.urls import path

app_name = "health_services"

urlpatterns = [
	path('', views.index),
]
