from django.db import models

class Employee(models.Model):
    Employee_ID = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Department = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    Place = models.CharField(max_length=100)

    def __str__(self):
        return self.Name