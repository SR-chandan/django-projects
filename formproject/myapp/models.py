from django.db import models


class student(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Place = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()