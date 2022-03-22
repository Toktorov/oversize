from django.urls import path 
from apps.settings.views import index, Errorhandler404



urlpatterns = [
    path('', index, name = "index"),
]

