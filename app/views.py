
from django.shortcuts import render, redirect, get_object_or_404

from django.utils import timezone

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
		
@unauthenticated_user
def signupPage(request: HttpRequest) -> HttpResponse:
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

@unauthenticated_user
def loginPage(request: HttpRequest) -> HttpResponse:
	if request.method == "POST":
		username = request.POST.get("username")
		password =request.POST.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("home")
		else:
			messages.info(request, "Username OR password is incorrect")
	context = {}
	return render(request, "login.html", context)

def logoutPage(request: HttpRequest) -> HttpResponse:
	logout(request)
	return redirect("login")

def homePage(request: HttpRequest) -> HttpResponse:
	context = {}
	return render(request, "home.html", context)

@login_required(login_url="login")
@admin_only
def adminPage(request: HttpRequest) -> HttpResponse:
    adoptions = Adoption.objects.all()
    owners = Owner.objects.all()
    total_adoptions = adoptions.count()
    adopted = adoptions.filter(note="Adopted").count()
    available = adoptions.filter(note="Available").count()
    context = {
        "adoptions": adoptions,
        "owners": owners,
        "total_adoptions": total_adoptions,
        "adopted": adopted,
        "available": available
    }
    
    return render(request, "admin.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["owner"])
def userPage(request: HttpRequest) -> HttpResponse:
	adoptions = request.user.owner.adoption_set.all()
	total_adoptions = adoptions.count()
	adopted = adoptions.filter(status="Adopted").count()
	available = adoptions.filter(status="Available").count()
	context = {"adoptions":adoptions, "total_adoptions":total_adoptions,
	"adopted":adopted,"available":available}
	return render(request, "user.html", context)

@login_required(login_url="login")
@allowed_users(allowed_roles=["owner"])
def settingsPage(request: HttpRequest) -> HttpResponse:
	owner = request.user.owner
	form = OwnerForm(instance=owner)
	if request.method == "POST":
		form = OwnerForm(request.POST, request.FILES,instance=owner)
		if form.is_valid():
			form.save()
	context = {"form":form}
	return render(request, "settings.html", context)

@login_required(login_url="login")
@allowed_users(allowed_roles=["admin", "owner"])
def petsPage(request):
    pets = Pet.objects.filter(status='Available')
    return render(request, 'pets.html', {'pets': pets})


@login_required
@allowed_users(allowed_roles=["owner"])
def adoptionPage(request, id):
    pet = get_object_or_404(Pet, id=id)
    adoption_form = AdoptionForm()
    if request.method == 'POST':
        adoption_form = AdoptionForm(request.POST)
        if adoption_form.is_valid():
            adoption = adoption_form.save(commit=False)
            adoption.pet = pet
            adoption.owner = pet.owner
            adoption.adopter = request.user
            adoption.status = 'Adopted'
            adoption.save()
            pet.status = 'Adopted'
            pet.owner = request.user.owner
            pet.save()
            return redirect('pets')
    return render(request, 'adoption.html', {'pet': pet, 'adoption_form': adoption_form})

@login_required
@admin_only
def createPetPage(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PetForm()

    return render(request, 'create.html', {'form': form})

@login_required
@admin_only
def deleteUserPage(request, id):
    user_in_question = get_object_or_404(User, id=id)
    if request.user.is_superuser and request.user != user_in_question:
        if request.method == "POST":
            owner_to_delete = Owner.objects.get(user=user_in_question)
            owner_to_delete.delete()
            user_in_question.delete()
            messages.success(request, 'User deleted successfully.')
            return redirect('dash')
        context = {'user_in_question': user_in_question}
        return render(request, 'delete.html', context)
    else:
        messages.error(request, 'Cannot delete an admin account or access this page.')
        return redirect('admin/')