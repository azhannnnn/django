from django import forms
from .models import Adhar,Allot


class AadharForm(forms.ModelForm):
    class Meta:
        model = Adhar
        fields = '__all__'


class AllotForm(forms.ModelForm):
    class Meta:
        model = Allot
        fields = '__all__'