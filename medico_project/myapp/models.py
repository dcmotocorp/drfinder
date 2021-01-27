
from django.db import models

# Create your models here.

class User(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    otp=models.IntegerField(default=456)
    is_active=models.BooleanField(default=True)
    is_varfied=models.BooleanField(default=False)
    role=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)
    first_time_login=models.BooleanField(default=False)

class Doctor(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic=models.FileField(upload_to='medico_expert/images/',blank=True,default='default.jpg')
    firstname=models.CharField(max_length=50,blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    about = models.CharField(max_length=500, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    contactno = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=70, blank=True)
    terms=models.BooleanField(default=False)

class Patient(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.FileField(upload_to='medico_expert/images/', blank=True, default='default.png')
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    contactno = models.CharField(max_length=50, blank=True)
    terms = models.BooleanField(default=False)
    address = models.CharField(max_length=100, blank=True)
    occupations = models.CharField(max_length=100, blank=True)

class appoint(models.Model):
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, blank=True)
    role=models.CharField(max_length=10, blank=True)
    contactno = models.CharField(max_length=50, blank=True)
    age = models.CharField(max_length=50, blank=True)

class add_test(models.Model):
    user_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    visitno = models.CharField(max_length=50, blank=True)
    testname = models.CharField(max_length=100, blank=True)
    discription = models.CharField(max_length=300,blank=True)



