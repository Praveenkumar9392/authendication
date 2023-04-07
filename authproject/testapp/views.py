from django.shortcuts import render
from django.contrib.auth.models import User
from testapp.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage_view(request):
    return render(request,'testapp/home.html')

@login_required
def javaexam_view(request):
    return render(request,'testapp/javaexam.html')
@login_required
def pythonexam_view(request):
    return render(request,'testapp/pythonexam.html')
@login_required
def aptitudeexam_view(request):
    return render(request,'testapp/apptitude.html')

def logout_view(request):
    return render(request,'testapp/logout.html')

def sign_up_view(request):
    form=Signupform()
    if request.method=="POST":
        form=Signupform(request.POST)
        User=form.save(commit=True)
        User.set_password(User.password)
        User.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
