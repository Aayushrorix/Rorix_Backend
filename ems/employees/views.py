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
                education_id = edu.get("education_id"),
                employee = employee,
                educationName = edu.get("educationName"),
                result = edu.get("universityName"),
                universityName = edu.get("result"),
                yearOfPassing = edu.get("yearOfPassing"),
            ).save()
        
        for exp in experienceDetails:
            ExperienceDetails.objects.create(
                experience_id = exp.get("experience_id"),
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
                    "education_id": edu.education_id,
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
                    "experience_id": exp.experience_id,
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


class DeteteEmployee(APIView):
    def delete(self,request,id):
        emp_id = id

        employee = Employee.objects.get(employee_id=emp_id)
        employee.personalDetails.delete()
        employee.bankDetails.delete()
        employee.professionalDetails.delete()
        employee.currentOrganizationDetails.delete()

        edus = EducationDetails.objects.filter(employee=employee)
        for edu in edus:
            edu.delete()
        exps = ExperienceDetails.objects.filter(employee=employee)
        for exp in exps:
            exp.delete()
        
        employee.delete()

        return Response({"deleted_employee_id":emp_id, "message":"Deleted Successfully"})


class EditEmployee(APIView):
    def put(self,request):

        data = request.data
        print("\n\n\n data ---> ",data)

        personalDetail = data.get("personalDetail")
        bankDetail = data.get("bankDetail")
        professionalDetail = data.get("professionalDetail")
        currentOrganizationDetail = data.get("currentOrganizationDetail")
        educationDetails = data.get("educationDetails")
        experienceDetails = data.get("experienceDetails")

        

        employee = Employee.objects.get(employee_id=data.get("id"))
        print("Done -> .................................")
        personalDetail_obj = employee.personalDetails
        bankDetail_obj = employee.bankDetails
        professionalDetail_obj = employee.professionalDetails
        currentOrganizationDetail_obj = employee.currentOrganizationDetails

        

        edu_objs = EducationDetails.objects.filter(employee=employee)
        exp_objs = ExperienceDetails.objects.filter(employee=employee)

        

        for edu in edu_objs:
            edu.delete()
        for exp in exp_objs:
            exp.delete()
        
        personalDetail_obj.firstName = personalDetail.get("firstName")
        personalDetail_obj.middleName =  personalDetail.get("middleName")
        personalDetail_obj.lastName =  personalDetail.get("lastName")
        personalDetail_obj.email =  personalDetail.get("email")
        personalDetail_obj.mobileNumber =  personalDetail.get("mobileNumber")
        # dob = personalDetail.get("dob"),
        personalDetail_obj.presentAddresss =  personalDetail.get("presentAddress")
        personalDetail_obj.permenentAddress =  personalDetail.get("permanentAddress")
        personalDetail_obj.copyAddress =  personalDetail.get("copyAddress")
        personalDetail_obj.save()

        bankDetail_obj.bankName = bankDetail.get("bankName")
        bankDetail_obj.accountName = bankDetail.get("accountName")
        bankDetail_obj.accountNumber = bankDetail.get("accountNumber")
        bankDetail_obj.ifscCode = bankDetail.get("ifscCode")
        bankDetail_obj.aadharNumber = bankDetail.get("aadhaarNumber")
        bankDetail_obj.panNumber = bankDetail.get("panNumber")
        bankDetail_obj.save()

        professionalDetail_obj.designation = professionalDetail.get("designation")
        professionalDetail_obj.department = professionalDetail.get("department")
        professionalDetail_obj.months = professionalDetail.get("years")
        professionalDetail_obj.years = professionalDetail.get("months")
        professionalDetail_obj.currentLocation = professionalDetail.get("currentLocation")
        professionalDetail_obj.save()

        currentOrganizationDetail_obj.currentCTC = currentOrganizationDetail.get("currentCTC")
        currentOrganizationDetail_obj.save()

        

        for edu in educationDetails:
            EducationDetails.objects.create(
                education_id = edu.get("education_id"),
                employee = employee,
                educationName = edu.get("educationName"),
                result = edu.get("universityName"),
                universityName = edu.get("result"),
                yearOfPassing = edu.get("yearOfPassing"),
            ).save()
        
        for exp in experienceDetails:
            ExperienceDetails.objects.create(
                experience_id = exp.get("experience_id"),
                employee = employee,
                companyName = exp.get("companyName"),
                position = exp.get("position"),
                totalYear = exp.get("totalYear"),
                lastCTC = exp.get("lastCTC"),
            ).save()
        
        employee.save()
        
        return Response(data)