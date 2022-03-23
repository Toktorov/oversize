from django.shortcuts import render, redirect
from apps.users.forms import UserCreateForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

class UserCreateView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('index')
    template_name = 'login.html'