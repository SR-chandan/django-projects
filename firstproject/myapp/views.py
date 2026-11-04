from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    a = "Welcome to Django!"
    return HttpResponse(a)
def view1(request):
    return HttpResponse("Welcome to Home Page")
def about(request):
    return HttpResponse("Welcome to About Page")
def contact(request):
    return HttpResponse("Welcome to Contact Page")
def services(request):
    return HttpResponse("Welcome to Services Page")