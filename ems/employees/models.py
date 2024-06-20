from django.db import models

# Create your models here.
class PersonalDetails(models.Model):
    firstName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField()
    mobileNumber = models.CharField(max_length=20) 
    dob = models.DateField()
    image = models.JSONField()
    presentAddresss = models.CharField(max_length=50)
    permenentAddress = models.CharField(max_length=50)
    copyAddress = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class BankDetails(models.Model):
    bankName = models.CharField(max_length=20)
    accountName = models.CharField(max_length=20)
    accountNumber = models.CharField(max_length=20)
    ifscCode = models.CharField(max_length=20)
    aadharNumber = models.CharField(max_length=20)
    panNumber = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProfessionalDetails(models.Model):
    designation = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    months = models.CharField(max_length=20)
    years = models.CharField(max_length=20)
    currentLocation = models.CharField(max_length=50)
    # skills = models.ExpressionList