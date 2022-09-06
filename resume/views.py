from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    skills = Techstack.objects.all()
    print(skills)
    projects = Projects.objects.all()

    context = {'skills':skills, 'projects':projects}

    return render(request, 'base/home.html',context)
