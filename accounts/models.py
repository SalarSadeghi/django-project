from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
Gender_CHIOCES = (
    ('m','Male'),
    ('f','Female'),
)
class CustomUser(AbstractUser):
    gender = models.CharField(max_length=1,choices=Gender_CHIOCES,blank=True,null=True)
    age = models.PositiveIntegerField(blank=True,null=True)
    university = models.CharField(max_length=50,blank=True,null=True)