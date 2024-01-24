from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Owner(models.Model): 
        profile_picture = models.ImageField(upload_to=None, null=True, blank=True)
        user = models.TextField()
        name = models.TextField()
        phone = models.CharField(max_length=13)
        pets = models.TextField()
        date_created = models.DateField(auto_now=False, auto_now_add=False)

class Type(models.Model):
        name = models.TextField()

class Pet(models.Model):
        picture = models.ImageField( upload_to=None, null=True)
        owner = models.TextField()
        name = models.TextField()
        age = models.IntegerField()
        gender = models.TextField(null=True)
        type = models.ForeignKey(Type, on_delete = models.CASCADE)
        description = models.TextField()


class Adoption(models.Model):
        owner = models.OneToOneField(Owner, on_delete = models.CASCADE)
        pet = models.OneToOneField(Pet, on_delete = models.CASCADE)
        status = models.TextField()
        note = models.TextField(null=True)
        date_created = models.DateTimeField()