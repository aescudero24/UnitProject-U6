from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# Create your forms here.

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		
class OwnerForm(ModelForm):
	class Meta:
		model = Owner
		fields = "__all__"
		exclude = ["user"]

class AdoptionForm(ModelForm):
	class Meta:
		model = Adoption
		fields = "__all__"
