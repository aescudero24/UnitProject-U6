
from django.shortcuts import render, redirect 

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from django.http.request import HttpRequest
from django.http.response import HttpResponse

from .models import *
from .forms import *
from .filters import *
from .decorators import *


# Create your views here.

#site home page
def homePage(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "home.html", context)
	#home

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
	#signup

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
	#login

#logout page
def logoutPage(request):
	logout(request)
	return redirect("login")

#admin dash page
@login_required
# @admin_only
def adminPage(request):
	owner = Owner.objects.all()
	if request.method == "POST":
		login_form = AuthenticationForm(request, request.POST)
		if login_form.is_valid():
			loginPage(request, login_form.get_user())
			return redirect('admin.html')

#pets page
@login_required
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
@login_required(login_url="login")
def settingsPage(request, pk):
	settings = Owner.objects.get(id=pk)
	form = UpdateForm(request.POST, instance=settings)
	if request.method == "POST":
		form = UpdateForm(request.POST, instance=settings)
		if form.is_valid():
			settings.save()
			return redirect('settings.html')
	context = {'form':form}
	return render(request, 'settings.html', context)
		
#create pet page
def createPetPage(request):
	if request.method == "POST":
		form = PetForm(request.POST, request.FILES)
		if form.is_valid():
			isinstance = form.save(commit = False)
			isinstance.user = request.user
			isinstance.save()
			return redirect("")
		#Create function: Lets the admin add in potential pets into the website
	else:
		form = PetForm()
		return render(request, 'create.html', {"form":form})

#DeleteUser
# @admin_only
def deleteUser(request, pk):
	user_inquestion = Owner.objects.get(id=pk)
	if request.user.is_superuser and request.user != user_inquestion:
		if request.method == "POST":
			user_inquestion.delete()
			return redirect('admin.html')
		context = {'user_inquestion': user_inquestion}
		return render(request, 'delete/', context)
	else:
		messages.error(request, 'Cannot delete an admin account...')
		return redirect('settings.html')

   	#delete function: lets the admin delete the user's account but the admin can't delete their own account
	

