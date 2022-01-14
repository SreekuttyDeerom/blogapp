from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.from django.http import HttpResponse


def index(request):
    return render(request,'home.html',{'name':'django'})

def add(request):
    value1 = int(request.POST['num1'])
    value2 = int(request.POST['num2'])
    res = value1 + value2
    return render(request,'home.html',{'result':res})
