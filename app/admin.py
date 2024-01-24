from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Owner)
admin.site.register(Type)
admin.site.register(Pet)
admin.site.register(Adoption) 