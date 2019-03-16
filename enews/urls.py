from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
app_name = "enews"

urlpatterns = [
	path('', views.index, name="enews"),
	path('/lecture', views.lecture_view, name="lecture"),
	path('/lecture/<int:id>', views.lecture_view, name="lecture")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
