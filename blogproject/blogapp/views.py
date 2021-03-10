from django.shortcuts import render

# Create your views here.s
def home(request) :
    return render(request, 'index.html')