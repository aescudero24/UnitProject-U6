from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import *

def owner_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='owner')
		instance.groups.add(group)
		Owner.objects.create(
			user=instance,
			name=instance.username,
			)

post_save.connect(owner_profile, sender=User)