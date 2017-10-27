from django.shortcuts import render

def index(request):
    return render(request,'main/home.html')

def login(request):
    return render(request,'main/login.html')