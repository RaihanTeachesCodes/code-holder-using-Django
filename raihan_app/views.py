from re import template
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from .models import raihanapps
from django.urls import reverse

def login(request):
    pass

def index(request):
    mymembers = raihanapps.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context,request))

def add(request):
    template2 = loader.get_template("add.html") 
    return HttpResponse(template2.render({}, request))

def home(request):
    template3= loader.get_template("main_screen.html")
    return HttpResponse(template3.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = raihanapps(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  table = raihanapps.objects.get(id=id)
  table.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = raihanapps.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = raihanapps.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))