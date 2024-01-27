from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Owner(models.Model): 
        profile_picture = models.ImageField(upload_to=None, null=True, blank=True)
        user = models.OneToOneField(User, on_delete = models.CASCADE)
        name = models.TextField()
        phone = models.CharField(max_length=13)
        date_created = models.DateField(auto_now=False, auto_now_add=False)

class Type(models.Model):
        name = models.TextField()

class Pet(models.Model):
        GENDER = (
                ('Male', 'Male'),
                ('Female', 'Female')
        )

        picture = models.ImageField(upload_to=None, null=True)
        owner = models.ForeignKey(User, on_delete = models.CASCADE)
        name = models.TextField()
        age = models.IntegerField()
        gender = models.TextField(null=True, choices=GENDER)
        type = models.ForeignKey(Type, on_delete = models.CASCADE)
        description = models.TextField()
        


class Adoption(models.Model):
        owner = models.OneToOneField(Owner, on_delete = models.CASCADE)
        pet = models.OneToOneField(Pet, on_delete = models.CASCADE)
        status = models.TextField()
        note = models.TextField(null=True)
        date_created = models.DateTimeField()