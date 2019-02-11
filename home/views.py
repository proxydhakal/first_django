from django.shortcuts import render

from .models import Home




def index(request):
    context ={
            'posts' :Home.objects.all()
        }
    return render(request,'home/home.html',context)

def about(request):
           return render(request,'home/about.html')