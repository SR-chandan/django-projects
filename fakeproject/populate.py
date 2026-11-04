
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fakeproject.settings")
django.setup()

from faker import Faker
from myapp.models import Employee

f = Faker('en-IN')

def generatepopulate(n):
    for i in range(n):

        fname = f.name()
        fage = f.random_int(min=20, max=50)
        femail = f.unique.email()
        fsalary = f.random_int(min=20000, max=100000)

        fdepartment = f.random_element(
            elements=('HR', 'IT', 'Finance', 'Sales')
        )

        fplace = f.city()

        femployee_id = f'E{f.unique.random_int(min=1000, max=9999)}'

        Employee.objects.create(
            Employee_ID=femployee_id,
            Name=fname,
            Age=fage,
            Department=fdepartment,
            Email=femail,
            Salary=fsalary,
            Place=fplace
        )

    print(n, "Employee records inserted successfully")


generatepopulate(20)
