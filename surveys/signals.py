from registration.signals import user_registered
from models import UserProfile
from django.contrib.auth.models import User


def createUserProfile(sender, instance, **kwargs):
    profile = users.models.UserProfile()
    profile.setUser(sender)
    profile.save()


user_registered.connect(createUserProfile, sender=User)
