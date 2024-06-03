from django import forms
from .models import Student

class Stu_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'