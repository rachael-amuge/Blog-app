from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class Meta:
    verbose_name_plural = "Post"


class NewUser(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=150, blank=True)
    profile_pic = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/', blank=True)

    def __str__(self):
        return self.user.username


def createUserProfile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
        user_profile.save()






