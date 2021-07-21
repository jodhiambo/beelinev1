from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required #added
# from .forms import UserUpdateForm, ProfileUpdateForm
from .forms import CustomUserCreationForm
from allauth.account.views import SignupView, LoginView


class MySignUpView(SignupView):
    template_name = 'users/signup.html'


class MyLoginView(LoginView):
    template_name = 'registration/login.html'

