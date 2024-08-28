from datetime import timezone
import datetime
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), max_length=150, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Info(models.Model):
    title = models.CharField('title', max_length = 50)
    anons = models.CharField('anons', max_length = 50)
    date = models.DateTimeField("date")
    
    def __str__(self):
        return self.title
    
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class Pysyntax(models.Model):
    content = models.CharField(max_length=3000)
    
    def __str__(self):
        return self.content
    
class DjangoInfo(models.Model):
    content = models.CharField(max_length=3000)
    
class Studying(models.Model):
    title = models.CharField(max_length=500, default=None)
    content = models.CharField(max_length=5000, default='')
    
    def __str__(self):
        return self.content

class FlaskInfo(models.Model):
    content = models.CharField(max_length=5000)
    
class Pyintro(models.Model):
    content= models.CharField(max_length=5000)