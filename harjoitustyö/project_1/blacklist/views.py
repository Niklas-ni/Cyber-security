from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Blacklist
import sqlite3
from django.db import connection


@login_required
def HomePageView(request):
    current_user = request.user
    accounts = Blacklist.objects.filter(owner= current_user)
    return render(request, 'blacklist/depts.html', {"accounts" : accounts})


def addView(request):
        current_user = request.user
        new_person = request.POST.get('person')
        new_dept = request.POST.get('dept')
        new_account = Blacklist.objects.create(owner=current_user,people=new_person,dept= new_dept)
        new_account.save()
        return redirect('/')

def removeView(request):
    remove_person = request.POST.get('person')
    cursor = connection.cursor()
    cursor.executescript("Update blacklist_blacklist SET dept = 0 Where people = '%s'" % remove_person)
    cursor.close()
    return redirect('/')

