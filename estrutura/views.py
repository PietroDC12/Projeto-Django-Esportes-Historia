from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def historia(request):
    return render(request, 'historia.html')