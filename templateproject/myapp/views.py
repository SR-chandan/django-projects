from django.shortcuts import render

# Create your views here.
def myview(request):
    return render(request,'myapp/index.html')
def myview1(request):
    return render(request,'myapp/index1.html')

def name(request):
    name = "Chandan"
    age = 24

    return render(request, 'name.html', {
        'name': name,
        'age': age
    })