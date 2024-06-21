from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class AddEmployee(APIView):

    def post(self,request):
        data = request.data
        # print("DATA : ===========>",data)

        personalDetail = data.get("personalDetail")
        bankDetail = data.get("bankDetail")
        professionalDetail = data.get("professionalDetail")
        currentOrganizationDetail = data.get("currentOrganizationDetail")
        educationDetails = data.get("educationDetails")
        experienceDetails = data.get("experienceDetails")

        personal = PersonalDetail.objects.create(
            firstName = personalDetail.get("firstName"),
            middleName =  personalDetail.get("middleName"),
            lastName =  personalDetail.get("lastName"),
            email =  personalDetail.get("email"),
            mobileNumber =  personalDetail.get("mobileNumber"),
            # dob = personalDetail.get("dob"),
            presentAddresss =  personalDetail.get("presentAddress"),
            permenentAddress =  personalDetail.get("permanentAddress"),
            copyAddress =  personalDetail.get("copyAddress"),
        )
        personal.save()

        bank = BankDetail.objects.create(
            bankName = bankDetail.get("bankName"),
            accountName = bankDetail.get("accountName"),
            accountNumber = bankDetail.get("accountNumber"),
            ifscCode = bankDetail.get("ifscCode"),
            aadharNumber = bankDetail.get("aadhaarNumber"),
            panNumber = bankDetail.get("panNumber"),
        )
        bank.save()
        
        professional = ProfessionalDetail.objects.create(
            designation = professionalDetail.get("designation"),
            department = professionalDetail.get("department"),
            months = professionalDetail.get("years"),
            years = professionalDetail.get("months"),
            currentLocation = professionalDetail.get("currentLocation"),
        )
        professional.save()

        currentOrganization = CurrentOrganizationDetail.objects.create(
            # joiningDate = currentOrganizationDetail.get("joiningDate"),
            # appraisalDate = currentOrganizationDetail.get("appraisalDate"),
            currentCTC = currentOrganizationDetail.get("currentCTC"),
        )
        currentOrganization.save()

        employee = Employee.objects.create(
            employee_id = data.get("id"),
            personalDetails = personal,
            bankDetails = bank,
            professionalDetails = professional,
            currentOrganizationDetails = currentOrganization,
        )
        employee.save()

        for edu in educationDetails:
            EducationDetails.objects.create(
                employee = employee,
                educationName = edu.get("educationName"),
                result = edu.get("universityName"),
                universityName = edu.get("result"),
                yearOfPassing = edu.get("yearOfPassing"),
            ).save()
        
        for exp in experienceDetails:
            ExperienceDetails.objects.create(
                employee = employee,
                companyName = exp.get("companyName"),
                position = exp.get("position"),
                totalYear = exp.get("totalYear"),
                lastCTC = exp.get("lastCTC"),
            ).save()
        
        return Response(data)


class GetEmployees(APIView):

    def get(self,request):

        all_employees = []

        employees = Employee.objects.all()

        for emp in employees:
            edu_list = []
            edus = EducationDetails.objects.filter(employee=emp)
            for edu in edus:
                edu_dict = {
                    "educationName": edu.educationName,
                    "universityName": edu.universityName,
                    "result": edu.result,
                    "yearOfPassing": edu.yearOfPassing,
                }
                edu_list.append(edu_dict)
            
            exp_list = []
            exps = ExperienceDetails.objects.filter(employee=emp)
            for exp in exps:
                exp_dict = {
                    "companyName": exp.companyName,
                    "position": exp.position,
                    "totalYear": exp.totalYear,
                    "lastCTC": exp.lastCTC,
                }
                exp_list.append(exp_dict)

            emp_dict = {
                "id": emp.employee_id,
                "personalDetail": {
                    "firstName": emp.personalDetails.firstName,
                    "middleName": emp.personalDetails.middleName,
                    "lastName": emp.personalDetails.lastName,
                    "email":emp.personalDetails.email,
                    "mobileNumber":emp.personalDetails.mobileNumber,
                    # "dob": "2000-11-10T18:30:00.000Z",
                    "presentAddress": emp.personalDetails.presentAddresss,
                    "permanentAddress": emp.personalDetails.permenentAddress,
                    "copyAddress": emp.personalDetails.copyAddress,
                },
                "bankDetail": {
                    "bankName": emp.bankDetails.bankName,
                    "accountName": emp.bankDetails.accountName,
                    "accountNumber": emp.bankDetails.accountNumber,
                    "ifscCode": emp.bankDetails.ifscCode,
                    "aadhaarNumber": emp.bankDetails.aadharNumber,
                    "panNumber": emp.bankDetails.panNumber,
                },
                "educationDetails": edu_list,
                "experienceDetails": exp_list,
                "professionalDetail":{
                    "designation": emp.professionalDetails.designation,
                    "department": emp.professionalDetails.department,
                    "years": emp.professionalDetails.years,
                    "months": emp.professionalDetails.months,
                    "currentLocation": emp.professionalDetails.currentLocation,
                },
                "currentOrganizationDetail":{
                    "currentCTC": emp.currentOrganizationDetails.currentCTC,
                }
            }

            all_employees.append(emp_dict)

        return Response({"employees":all_employees})