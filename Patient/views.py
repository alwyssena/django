from django.shortcuts import render,redirect
from . models import *
from . forms import *

# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    form=Patient_forms()
    if request.method=='POST':
        form=Patient_forms(request.POST,request.FILES)
        if form.is_valid():
                form.save(commit=True)
                return redirect('login/')
    return render(request,"patient\Home.html",{'form':form})
def login(request):
    data=Patient_model.objects.all()
    print(data)
    return render(request,"patient\Details.html",{'data':data})
