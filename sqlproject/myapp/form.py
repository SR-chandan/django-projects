from django import forms

class studentform(forms.Form):
    Name = forms.CharField()
    Age = forms.IntegerField()
    Place = forms.CharField()
    email = forms.EmailField()
    dob = forms.DateField()