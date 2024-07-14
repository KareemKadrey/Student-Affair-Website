from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members
from django.shortcuts import render

def start(request):
    return render (request,'choosing.html')
def new(request):
    return render (request,'home.html')
def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))
  
def addrecord(request):
    a = request.POST['Name']
    b = request.POST['ID']
    c = request.POST['Gpa']
    d = request.POST['Level']
    e = request.POST['Department']
    f = request.POST['Status']
    g = request.POST['Gender']
    h = request.POST['Phone']
    i  = request.POST['Email']
    j = request.POST['Birth_Date']


    member = Members(Name=a, ID=b,Gpa = c,Level=d,Department = e,Status = f,
    Gender = g , Phone = h,Email = i,Birth_Date = j)
    member.save()
    return HttpResponseRedirect(reverse('index'))
def delete(request, id):
    member = Members.objects.get(ID=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))
def update(request, id):
    mymember = Members.objects.get(ID=id)
    template = loader.get_template('update.html')
    context = {
    'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))
def updaterecord(request, id):
    a = request.POST['Name']
    b = request.POST['ID']
    c = request.POST['Gpa']
    d = request.POST['Level']
    e = request.POST['Department']
    f = request.POST['Status']
    g = request.POST['Gender']
    h = request.POST['Phone']
    i  = request.POST['Email']
    j = request.POST['Birth_Date']
    member = Members.objects.get(ID=id)
    member.Name = a
    member.ID = b
    member.Gpa = c
    member.Level = d
    member.Department = e
    member.Status = f
    member.Gender = g
    member.Phone = h
    member.Email = i
    member.Birth_Date = j
    member.save()
    return HttpResponseRedirect(reverse('index'))
def active(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('Active.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
