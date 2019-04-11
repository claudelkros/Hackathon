from . import views
from django.urls import path

app_name = "VOIP"

urlpatterns = [
	path('', views.index, name="VOIP")]