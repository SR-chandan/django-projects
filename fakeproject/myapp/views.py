from django.shortcuts import render
from myapp.models import Employee

def fake(request):
    s=Employee.objects.all()
    d={'emp':s}
    return render (request,'employe.html',d)