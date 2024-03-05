from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *
from . forms import *

# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    form=Doctor_forms()
    if request.method=='POST':
        form=Doctor_forms(request.POST,request.FILES)
        if form.is_valid():
                form.save(commit=True)
                
                return redirect('login/')
                
    return render(request,"Doctor\Home.html",{'form':form})
def login(request):
    data=Doctor_model.objects.all()
    print(data)
    return render(request,"Doctor\Details.html",{'data':data})
