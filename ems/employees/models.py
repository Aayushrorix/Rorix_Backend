from django.db import models

# Create your models here.
class PersonalDetail(models.Model):
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    mobileNumber = models.CharField(max_length=50) 
    dob = models.DateField(null=True,blank=True)
    # image = models.JSONField()
    presentAddresss = models.CharField(max_length=50)
    permenentAddress = models.CharField(max_length=50)
    copyAddress = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class BankDetail(models.Model):
    bankName = models.CharField(max_length=50)
    accountName = models.CharField(max_length=50)
    accountNumber = models.CharField(max_length=50)
    ifscCode = models.CharField(max_length=50)
    aadharNumber = models.CharField(max_length=50)
    panNumber = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProfessionalDetail(models.Model):
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    months = models.CharField(max_length=50)
    years = models.CharField(max_length=50)
    currentLocation = models.CharField(max_length=50)
    skills = models.CharField(max_length=100,default="")
    # resumeFile = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CurrentOrganizationDetail(models.Model):
    joiningDate = models.DateField(null=True,blank=True)
    appraisalDate = models.DateField(null=True,blank=True)
    currentCTC = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employee(models.Model):
    employee_id = models.CharField(max_length=50,unique=True)
    personalDetails = models.ForeignKey(PersonalDetail,on_delete=models.CASCADE)
    bankDetails = models.ForeignKey(BankDetail,on_delete=models.CASCADE)
    professionalDetails = models.ForeignKey(ProfessionalDetail,on_delete=models.CASCADE)
    currentOrganizationDetails = models.ForeignKey(CurrentOrganizationDetail,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EducationDetails(models.Model):
    education_id = models.IntegerField(null=True,blank=True,unique=True)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    educationName = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    universityName = models.CharField(max_length=50)
    yearOfPassing = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ExperienceDetails(models.Model):
    experience_id = models.IntegerField(null=True,blank=True,unique=True)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    companyName = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    totalYear = models.CharField(max_length=50)
    lastCTC = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)