from django.contrib import admin
from . models import *
# Register your models here.
class Patient_admin(admin.ModelAdmin):
    l=['first_name','last_name','Picture','username','Email_id','password',' confirm_password','line_1','city','state','pincode']
admin.site.register(Patient_model,Patient_admin)