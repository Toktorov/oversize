from django.urls import path 
from apps.users.views import UserCreateView


urlpatterns = [
    path('login/', UserCreateView.as_view(), name = "register_user")
]