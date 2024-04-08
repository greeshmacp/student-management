from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    usertype = models.CharField(max_length=50)


class Teacher(models.Model):
    tname = models.CharField(max_length=30, default='Unknown')
    department = models.CharField(max_length=30)
    status = models.CharField(max_length=30, default='block')
    tid = models.ForeignKey(User, on_delete=models.CASCADE)


class Student(models.Model):
    sname = models.CharField(max_length=30, default='Unknown')
    department = models.CharField(max_length=30)
    status = models.CharField(max_length=30, default='block')
    sid = models.ForeignKey(User,on_delete=models.CASCADE)
    tea = models.CharField(max_length=50, default='None')


class Leave(models.Model):
    sfrom = models.CharField(max_length=30, default='Unknown')
    totea = models.CharField(max_length=50, default='None')
    date = models.DateField()
    msg = models.CharField(max_length=255)
    status = models.CharField(max_length=30, default='NotApproved')