from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request,'index.html')

def chat(request):
    return render(request,'chatbox.html')

def home(request):
    return render(request,'homepage.html')

def personaldetail(request):
    return render(request,'personaldetails.html')

def homep_enroll(request):
    return render(request,'homep_enroll.html')
