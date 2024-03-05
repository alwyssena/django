from django.db import models

# Create your models here.
class Doctor_model(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    Picture=models.ImageField(null=True,blank=True, upload_to='img/')
    username=models.CharField(max_length=30)
    Email_id=models.EmailField()
    password=models.CharField(max_length=30)
    confirm_password=models.CharField(max_length=30)
    line_1=models.CharField(max_length=200)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=50)
    pincode=models.PositiveIntegerField()