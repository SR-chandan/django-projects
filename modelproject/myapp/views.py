from django.shortcuts import render
from myapp.models import Employee

def student_list(request):
    s = Employee.objects.all()
    d = {'Student': s}
    return render(request, 'student.html', d)