from django import forms
from Doctor.models import *
class Doctor_forms(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    Picture=forms.ImageField(widget=forms.ClearableFileInput)

    class Meta:
        model=Doctor_model
        fields='__all__'