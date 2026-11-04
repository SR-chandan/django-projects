from django.shortcuts import render
from django.http import HttpResponse

def add(request):
    a = int(input("enter a n1:"))
    b = int(input("enter a n2:"))
    c = a + b
    return HttpResponse(str(c))
def sub(request):
    a = int(input("enter a n1:"))
    b = int(input("enter a n2:"))
    c = a - b
    return HttpResponse(str(c))
