from django.shortcuts import render, redirect
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# landing page view function

def homepage(request):

    return render(request, 'websiteapp/index.html')