#-----------------------------------
# coding:   utf-8                  
# Author:   zhangwei               
# Time:     2019/12/6 17:15        
# Filename: view.py 
# Notes：               
#-----------------------------------

from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello, Django!</h1>')