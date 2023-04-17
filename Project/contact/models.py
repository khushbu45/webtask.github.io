from django.db import models

class contactEnquiry(models.Model):
    name=models.CharField(max_length=50,default='True')
    email=models.CharField(max_length=50,default='True')
    phone=models.CharField(max_length=50,default='True')
    message=models.TextField(max_length=50,default='True')

# Create your models here.
