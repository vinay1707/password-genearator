from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'gen/home.html')

def about(request):
    return render(request,'gen/about.html')


def password (request):

    char=list(' ')
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('lowercase'):
        char.extend(list('abcdefghijklmnopqrstuvwxyz'))

    if request.GET.get('special'):
        char.extend(list('!@#$%^&*'))

    if request.GET.get('numbers'):
        char.extend(list('123456789'))



    length= int(request.GET.get('length',12 ))

    password=' '
    for x in range(length):
        password += random.choice(char)



    return render(request,'gen/password.html',{'password': password})