
from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .models import *
from .forms import *
from .filters import *


# Create your views here.

#admin only page
def dashboardPage(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "dashboard.html", context)

#user only page
def homePage(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "home.html", context)

#login page
def loginPage(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "login.html", context)

#sign up page
def signupPage(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "signup.html", context)

#logout page
def logoutPage(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("login")