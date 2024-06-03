from django import forms
from .models import Student

class SyudentRegistration(forms.Form):
    first_name = forms.CharField(max_length=15,min_length=5,error_messages={'required':"Enter your Name"}) # _ converted into space and first charector converted into Uppercase
    email = forms.EmailField(label='Your Email',label_suffix='',initial='neeraj@gmail.com')
    # email = forms.EmailField(label='Your Email',label_suffix='')
    contact = forms.CharField(help_text='limit 20 char',)
    password = forms.CharField(widget=forms.PasswordInput) # bydefalut required is True






# class SyudentRegistration(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = '__all__'

    # Individual field validation
    # def clean_first_name(self):
    #     fname=self.cleaned_data['first_name']
    #     if len(fname)<4:
    #         raise forms.ValidationError('Name must be eaual or grater then 4 charactors')
    #     return fname
    # def clean_email(self):
    #     email=self.cleaned_data['email']
    #     if len(email)<15:
    #         raise forms.ValidationError('Email must be eaual or grater then 15 charactors')
    #     return email
    # def clean_contact(self):
    #     contact=self.cleaned_data['contact']
    #     if len(contact)!=10:
    #         raise forms.ValidationError('Contact must be eaual to 10 digits')
    #     return contact
    # def clean_password(self):
    #     password=self.cleaned_data['password']
    #     if len(password)<8:
    #         raise forms.ValidationError('Password must be greater then 8 characters')
    #     return password