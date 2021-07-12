from django.db import models

# Create your models here.

class Customer(models.Model) : 
    GENDER_CHOICES = (('Male','Male'),('Female', 'Female') ) 
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES) 
    age = models.IntegerField() 
    salary = models.IntegerField()