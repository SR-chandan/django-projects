from django import forms
from myapp.models import student


class studentform(forms.ModelForm):
    class Meta:
        model = student
        fields = ['Name', 'Age', 'Place', 'email', 'dob']

    def clean_Name(self):
        n = self.cleaned_data['Name']
        if len(n)<3:
            raise forms.ValidationError("Name should be more than 3 characters")
        return n        