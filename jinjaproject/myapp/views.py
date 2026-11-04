from django.shortcuts import render

# Create your views here.
def home(request):
    name = "Chandan"
    age = 24
    place = "Banglore"

    ctx={
        'Name': name,
        'Age': age,
        'PLACE':place
    }
    return render(request,'myapp/jinja.html',ctx)