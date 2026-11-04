from django.shortcuts import render

def home(request):
    return render(request,'myapps/pro1.html')