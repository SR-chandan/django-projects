from django.db import models

class student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    email=models.EmailField()