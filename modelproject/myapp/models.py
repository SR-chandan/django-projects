from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=30)
    employee_id = models.CharField(max_length=20)
    department = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.name