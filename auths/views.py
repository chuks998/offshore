from django.shortcuts import render
# Create your views here.

#loginView
from django.contrib.auth.views import LoginView    

class Login(LoginView):
    template_name = 'login_form.html'