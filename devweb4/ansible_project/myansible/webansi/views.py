from django.shortcuts import render,HttpResponse

# Create your views here.

def  mainpage(request):
    return render(request,'webansi/base.html')

def index(request):
    return  render(request,'webansi/base.html')

def addhosts(request):
    return   HttpResponse('add hosts')

def  addmodules(request):
    return  HttpResponse('add modules')

def tasks(request):
    return  HttpResponse('execute task')