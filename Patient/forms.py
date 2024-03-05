from django import forms
from Patient.models import *
class Patient_forms(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    Picture=forms.ImageField(widget=forms.ClearableFileInput)

    class Meta:
        model=Patient_model
        fields='__all__'