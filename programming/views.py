# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from programming.models import Student_details, Groups
from django.views.generic import ListView
import re
# Create your views here.

def addStudent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        codechef = request.POST.get('codechef')
        codeforces = request.POST.get('codeforces')
        year = request.POST.get('year')
        u =  Student_details(name = name, codechef = codechef, codeforces = codeforces, year = year)
        u.save()
        groupname = Groups.objects.get(groupname = "Bios").id
        u.groupid.add(groupname)
        u.save()
        return HttpResponseRedirect('/programming/addStudent')
    return render(request, 'programming/addstudent.html',{})

class viewsummary(ListView):
    model = Student_details
    template_name = 'programming/viewsummary.html'

def addgroup(request):
    if request.method == 'POST':
        groupname = request.POST.get('name')
        students = request.POST.getlist('students[]')
        u = Groups(groupname = groupname, students=students)
        u.save()
        for i in students:
            stu = Student_details.objects.get(name = i)
            stu.groupid.add(u.id)
        return HttpResponseRedirect('/programming/addStudent')
    return render(request, 'programming/creategroup.html',{'name':Student_details.objects.values_list('name',flat=True)})

def viewgroups(request):
    if request.method == 'POST':
        delstu = request.POST.getlist('delete[]')
        for i in delstu:
            stu = Groups.objects.get(groupname = i)
            stu.delete()
    return render(request, 'programming/viewgroups.html',{'groupname':Groups.objects.values_list('groupname', flat=True)})

def deleteStudents(request):
    if request.method == 'POST':
        delstu = request.POST.getlist('deletestu[]')
        for i in delstu:
            stu = Student_details.objects.get(name = i)
            stu.delete()
    return render(request, 'programming/deletestudents.html',{'stuname':Student_details.objects.values_list('name', flat=True)})

def detailGroup(request, slug):
    stu = Groups.objects.get(groupname=slug)
    detail= []
    print stu
    #for i in stu:

    return render(request, 'programming/detailview.html',{'grpstu':detail})
