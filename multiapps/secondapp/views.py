from django.shortcuts import render

from django.http import HttpResponse

def app2(request):
    return HttpResponse("I am in secondapp")