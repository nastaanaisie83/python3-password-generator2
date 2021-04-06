from django.shortcuts import render
from django.http import HttpResponse;
# Create your views here.
import random

def home(request):

    return render(request, 'generator/home.html', {'password': 'work here'});
def password(request):
    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))
    if request.GET.get('specialCharacters'):
            characters.extend(list('#@!%&*'))
    length = int(request.GET.get('length'))
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})

def aboutUs(request):
    return render(request, 'generator/aboutUs.html')
