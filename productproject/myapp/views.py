from django.shortcuts import render
from myapp.models import products

def view1(request):
    p = products.objects.all()
    d = {'prod': p}

    return render(request, 'iphone.html', d)