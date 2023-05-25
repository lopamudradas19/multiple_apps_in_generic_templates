from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def third(request):
    return HttpResponse('This is my third FVB')
def home2(request):
    return render(request,'home2.html')