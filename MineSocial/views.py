# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def welcome (request):
    return render (request,'welcome.html',{'current_date_time': datetime.now})
def login (request):
    return render (request,'login.html')