from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"shop/index.html")

def about(request):
    return HttpResponse("<H1>Crimson About</H1>")

def login(request):
    return render(request,"shop/login.html")

def signup(request):
    return render(request,"shop/signup.html")