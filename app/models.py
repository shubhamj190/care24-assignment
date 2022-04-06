from pyexpat import model
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from cloudinary.models import CloudinaryField
# Create your models here.

class CustomUser(AbstractUser):
    # If we use say AbstractBaseUser then we have to give permissionMixiin that is

    USER_ROLES=(
        ('ADMIN','ADMIN'),
        ('AUTHOR','AUTHOR'),
    )

    email=models.EmailField(unique=True)
    Phone=models.CharField(max_length=10)
    address=models.CharField(max_length=255,null=True, blank=True)
    city=models.CharField(max_length=255,null=True, blank=True)
    state=models.CharField(max_length=255,null=True, blank=True)
    country=models.CharField(max_length=255,null=True, blank=True)
    pincode=models.CharField(max_length=6)
    user_type=models.CharField(choices=USER_ROLES, max_length=16, default='AUTHOR')
    username=None

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
    objects=CustomUserManager()

    def __str__(self) -> str:
        return self.email

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name    


class Content(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField(blank=True, null=True)
    summary=models.CharField(max_length=255)
    document=CloudinaryField(resource_type="auto", null=True, blank=False)
    categories=models.ManyToManyField(Category)
    author=models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title



    