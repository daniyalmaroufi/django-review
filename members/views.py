from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models
from django.db.models import Q

def members(request):
    template=loader.get_template('first.html')
    theadmin=models.Member.objects.filter(Q(firstname__startswith='dan')|Q(firstname='danial'))
    context={
        'theadmin':theadmin.values()[0],
    }
    return HttpResponse(template.render(context,request))

def all_members(request):
    members=models.Member.objects.values_list('firstname','lastname','slug').order_by('-firstname')
    context={
        'members':members.values(),
    }
    template=loader.get_template('all_members.html')
    return HttpResponse(template.render(context,request))


def details(request,slug):
    member=models.Member.objects.get(slug=slug)
    context={
        'member':member,
    }
    template=loader.get_template('details.html')
    return HttpResponse(template.render(context,request))

def fruits(request):
    fruits=['apple','banana','mango','orange']
    context={
        'fruits':fruits,
    }
    template=loader.get_template('fruits.html')
    return HttpResponse(template.render(context,request))


