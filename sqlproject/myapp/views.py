from django.shortcuts import render
from myapp.form import studentform
from myapp.models import *
# Create your views here.
def fun1(request):
    s= student.objects.all()
    d = {'stud':s}
    return render (request,'index.html',d)
def formview(request):
    f = studentform()
    if request.method == 'POST':
        f = studentform(request.POST)
        if f.is_valid():
            return render(request,'success.html')
    d = {'form':f}
    return render(request,'form.html',d)    