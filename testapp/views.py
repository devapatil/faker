from django.shortcuts import render
from testapp.models import Employee

def emp_view(request):
    employees=Employee.objects.all()
    return render(request,'result.html',{'employees':employees})
