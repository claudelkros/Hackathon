from . import views
from django.urls import path

app_name = "health_services"

urlpatterns = [
	path('', views.index, name="health_services"),
	path('pharmacie', views.pharmacie_view, name='pharmacie'),
	path('medecinenaturelle', views.medecinenaturel_view, name='medecinenaturelle'),
	path('premiersoins', views.premiersoins_view, name='premiersoins')
]
