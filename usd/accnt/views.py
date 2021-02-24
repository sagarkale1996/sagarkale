from django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def rt(request):
    form=UserCreationForm()
    context={'form':form}
    return render(request,'render.html',context)
def komal():
    pass
def pappa():
    pass
def sagar():
    pass
def indra():
    pass




