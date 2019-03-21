from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
app_name = "learning"

urlpatterns = [
	path('', views.index, name="learning"),
	path('/learningnews', views.learningnews, name="learningNews"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
