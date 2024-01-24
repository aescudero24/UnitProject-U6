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



class OwnerForm(forms.ModelForm):
	class Meta:
		model = User
		fields = "__all__"
		exclude = ["date_created"]
	
class TypeForm(forms.Form):
	name = forms.CharField()
	
class PetForm(forms.Form):
	owner = forms.CharField()
	name = forms.CharField()
	age = forms.IntegerField()
	gender = forms.CharField()
	description = forms.CharField()
	
class AdoptionForm(forms.ModelForm):
	class Meta:
		model = User
		fields = "__all__"
