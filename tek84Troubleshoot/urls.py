from django.urls import path
from . import views


# URLConf
urlpatterns = [
	path('index/', views.index, name='index'),
	path('errors/', views.errors, name='errors'),
]