from django.shortcuts import render

def index(request):
    return render(request, 'base/principal.html')

def login(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'register.html')

