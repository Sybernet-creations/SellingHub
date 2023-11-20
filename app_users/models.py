from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

import pycountry

countries = list(pycountry.countries)
COUNTRY = []
for country in countries:
    my_country = (country.name,country.name)
    COUNTRY.append(my_country)


# Create your models here.

#"""payment method model"""
class Payement(models.Model):
    payement_method = models.CharField(max_length=100,blank=False,unique=True)
    def __str__(self):
        return self.payement_method

#"""Programming language model"""
class Language(models.Model):
    name = models.CharField(max_length=100,unique=True,blank=False)
    level = models.CharField(max_length=100,
                             choices=(
                                 ('Biginner','Biginner'),('Intermidiate','Intermidiate'),('Advance','Advance')
                             ),blank=False)
    def __str__(self):
        return f'{self.level} : {self.name}'
    


    
# customers
class Customer(AbstractUser):
    contact_number = PhoneNumberField()
    nationality = models.CharField(max_length=100,blank=False,choices=COUNTRY)
    zip_code = models.CharField(max_length=100,blank=False)
    city = models.CharField(max_length=100,blank=False)
    
    
