from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.

class Provider (models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    middle_name = models.CharField(max_length=200, blank = True)
    last_name = models.CharField(max_length=200, blank=False)
    gender_choices = (
        ('M','Male'),('F','Female'),
        )
    gender = models.CharField(max_length = 2, choices = gender_choices,)
    mobile_no = models.BigIntegerField (validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)], blank= False,)
    postgraduation_degree = models.CharField (max_length=200, blank = True)
    clinic_name = models.CharField (max_length=200, blank = True)
    address1 = models.CharField (max_length=200, blank = True)
    address2 = models.CharField (max_length=200, blank = True)
    pincode = models.CharField (max_length=6, blank = True)
    city = models.CharField (max_length=50, blank = True)
    state = models.CharField (max_length=50, blank = True)
    clinic_contact_no = models.BigIntegerField (validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)], blank = True, null=True)
    services = models.CharField (max_length=1000, blank = True)
    profile_name = models.CharField (max_length=50, primary_key=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url (self):
        return reverse('provider_profile', args=[str(self.profile_name)]) #this is basically url for each entry in the model