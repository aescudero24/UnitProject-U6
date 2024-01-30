
from django.shortcuts import render, redirect 

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
		
# @unauthenticated_user
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

# @unauthenticated_user
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

# @login_required(login_url="login")
# @admin_only
def adminPage(request: HttpRequest) -> HttpResponse:
	adoptions = Adoption.objects.all()
	owners = Owner.objects.all()
	total_adoptions = adoptions.count()
	adopted = adoptions.filter(status="Adopted").count()
	available = adoptions.filter(status="Available").count()
	context = {"adoptions":adoptions, "owners":owners,
	"total_adoptions":total_adoptions,"adopted":adopted,
	"available":available }
	return render(request, "admin.html", context)

# @login_required(login_url="login")
# @allowed_users(allowed_roles=["student"])
def userPage(request: HttpRequest) -> HttpResponse:
	adoptions = request.user.owner.adoption_set.all()
	total_adoptions = adoptions.count()
	adopted = adoptions.filter(status="Adopted").count()
	available = adoptions.filter(status="Available").count()
	context = {"adoptions":adoptions, "total_adoptions":total_adoptions,
	"adopted":adopted,"available":available}
	return render(request, "user.html", context)

# @login_required(login_url="login")
# @allowed_users(allowed_roles=["student"])
def settingsPage(request: HttpRequest) -> HttpResponse:
	owner = request.user.owner
	form = OwnerForm(instance=owner)
	if request.method == "POST":
		form = OwnerForm(request.POST, request.FILES,instance=owner)
		if form.is_valid():
			form.save()
	context = {"form":form}
	return render(request, "settings.html", context)

# @login_required(login_url="login")
# @allowed_users(allowed_roles=["admin"])
def petsPage(request: HttpRequest) -> HttpResponse:
	pets = Pet.objects.all()
	return render(request, "pets.html", {"pets":pets})

# @login_required(login_url="login")
# @allowed_users(allowed_roles=["admin"])
# def ownerPage(request, id):
# 	owner = Owner.objects.get(id=id)
# 	adoptions = owner.adoption_set.all()
# 	adoptions_count = adoptions.count()
# 	myFilter = AdoptionFilter(request.GET, queryset=adoptions)
# 	adoptions = myFilter.qs 
# 	context = {"owner":owner, 'adoptions':adoptions, "adoptions_count":adoptions_count,
# 	"myFilter":myFilter}
# 	return render(request, "owner.html",context)

# # @login_required(login_url="login")
# # @allowed_users(allowed_roles=["admin", "student"])
# def addPetPage(request, id):
# 	AdoptionsFormSet = inlineformset_factory(Student, Booking, fields=("book", "status"), extra=10 )
# 	student = Student.objects.get(id=id)
# 	formset = BookingFormSet(queryset=Booking.objects.none(),instance=student)
# 	if request.method == "POST":
# 		form = BookingForm(request.POST)
# 		formset = BookingFormSet(request.POST, instance=student)
# 		if formset.is_valid():
# 			formset.save()
# 			return redirect("/")
# 	context = {"form":formset}
# 	return render(request, "accounts/booking_form.html", context)

# # @login_required(login_url="login")
# # @allowed_users(allowed_roles=["admin", "student"])
# def updateAdoptionPage(request, id):
# 	adoption = Adoption.objects.get(id=id)
# 	form = AdoptionForm(instance=adoption)
# 	if request.method == "POST":
# 		form = AdoptionForm(request.POST, instance=adoption)
# 		if form.is_valid():
# 			form.save()
# 			return redirect("home")
# 	context = {"form":form}
# 	return render(request, "adoption_form.html", context)

# # @login_required(login_url="login")
# # @allowed_users(allowed_roles=["admin", "student"])
# def deleteAdoptionPage(request, id):
# 	adoption = Adoption.objects.get(id=id)
# 	if request.method == "POST":
# 		adoption.delete()
# 		return redirect("home")
# 	context = {"adoption":adoption}
# 	return render(request, "delete.html", context)

#create pet page
def createPetPage(request: HttpRequest) -> HttpResponse:
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
		return render(request, 'delete', context)
	else:
		messages.error(request, 'Cannot delete an admin account...')
		return redirect('settings/')

   	#delete function: lets the admin delete the user's account but the admin can't delete their own account
	
	#######################################################################################################

