from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Owner(models.Model):
        user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
        name = models.CharField(max_length=200, null=True)
        phone = models.CharField(max_length=13, null=True)
        profile_pic = models.ImageField(upload_to="profile_pics", default="images/profile1.png", null=True, blank=True)
        date_created = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
                return self.name


class Type(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Pet(models.Model):
        GENDER = (
		('Male', 'Male'),
		('Female', 'Female'),
	)
        STATUS = (
        ('Adopted', 'Adopted'),
        ('Available', 'Available'),
	)
        name = models.CharField(max_length=200, null=True)
        age = models.IntegerField()
        gender = models.CharField(max_length=200, null=True, choices=GENDER)
        description = models.CharField(max_length=1000, null=True)
        pet_pic = models.ImageField(upload_to="pets_pics")
        status = models.CharField(max_length=200, default="Available", choices=STATUS)
        owner = models.ForeignKey(Owner, null=True, on_delete=models.CASCADE)
        date_created = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
                return self.name

class Adoption(models.Model):
    owner = models.ForeignKey(Owner, null=True, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, null=True, on_delete=models.CASCADE)
    adopter = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.pet.name


