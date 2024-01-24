from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Owner(models.Model): 
        profile_picture = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
        user = models.TextChoices()
        name = models.TextChoices()
        phone = models.CharField(_(""), max_length=13)
        pets = models.TextChoices()
        date_created = models.DateField(_(""), auto_now=False, auto_now_add=False)

class Pet(models.Model):
        picture = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
        owner = models.TextField()
        name = models.TextField()
        age = models.IntegerField()
        gender = models.TextField()
        type = models.TextField()
        description = models.TextField()

class Type(models.Model):
        name = models.TextField()

class Adoption(models.Model):
        owner = models.TextField()
        pet = models.OneToOneField()
        status = models.TextField()
        note = models.TextField()
        date_created = models.DateTimeField()