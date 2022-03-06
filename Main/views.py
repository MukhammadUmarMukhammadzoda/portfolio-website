from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def index(request):
    skill = Skills.objects.all()
    doneprojects = DoneProjects.objects.all()
    chronology = Chronology.objects.all()
    contact = Contact.objects.all()
    
    data = {
        'skills':skill,
        'doneprojects':doneprojects,
        'chronology': chronology,
        'contact':contact
    }
    return render(request,'index.html',data)