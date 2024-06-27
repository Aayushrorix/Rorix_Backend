from django.urls import path
from .views import *


urlpatterns = [
    path('add_employee',AddEmployee.as_view()),
    path('get_employees',GetEmployees.as_view()),
    path('delete/<str:id>',DeteteEmployee.as_view()),
    path('update',EditEmployee.as_view()),
]