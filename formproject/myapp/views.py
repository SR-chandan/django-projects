from django.shortcuts import render
from django.http import HttpResponse
from myapp.form import studentform
from myapp.models import student


def formview(request):
    f = studentform()

    if request.method == 'POST':
        f = studentform(request.POST)

        if f.is_valid():
            f.save()

            s = student.objects.all()
            d = {'data': s}

            return render(request, '1.html', d)

    d = {'form': f}
    return render(request, 'form.html', d)