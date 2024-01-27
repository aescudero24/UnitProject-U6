
from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .models import *
from .forms import *
from .filters import *
from .decorators import *


# Create your views here.

#home page
@login_required
# @allowed_users(allowed_roles=[""])
def homePage(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "home.html", context)

#signup page
@unauthenticated_user
def signupPage(request):
	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get("username")
			messages.success(request, "Account was created for " + username)
			return redirect("login")
	context = {"form":form}
	return render(request, "signup.html", context)

#login page
@unauthenticated_user
def loginPage(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("dash")
		else:
			messages.info(request, "Username OR password is incorrect")
	context = {}
	return render(request, "login.html", context)

#logout page
def logoutPage(request):
	logout(request)
	return redirect("login")

#admin dash page
@login_required
# @admin_only
def adminPage(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "admin.html", context)

#pets page
@login_required
#@admin_only
def petsPage(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "pets.html", context) 

#owner page
@login_required
#@admin_only
def ownerPage(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "owner.html", context) 

#user dash page
@login_required
#@allowed_users(allowed_roles=["owner"])
def userPage(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "user.html", context)

#settings page
@login_required
#@allowed_users(allowed_roles=["owner"])
def settingsPage(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "settings.html", context)

#adoption page
@login_required
# @admin_only
def adoptionPage(request):
	...

#this is basically the create order
@login_required
# @admin_only
def CreatingPet(request):
	if request.method == "POST":
		form = PetForm(request.POST, request.FILES)
		if form.is_valid():
			isinstance = form.save(commit = False)
			isinstance.user = request.user
			isinstance.save()
			return redirect("")
	else:
		form = PetForm()
		return render(request, 'create.html', {"form":form})

def deleteUser(request, pk):
	the_user = Owner.objects.get(id=pk)
	if request.method == "POST":
		the_user.delete()
		return redirect('admin.html')
	context = {'user_inquestion': the_user}
	return render(request, 'delete/', context)
	
