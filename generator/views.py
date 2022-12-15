from django.shortcuts import render
import random
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    low_charachter = list('abcdifghrtoyumnbqzx')

    if request.GET.get('uppercase'):
        low_charachter.extend(list('ASDFGHJKLQWERTYUIOPZXCVBNM'))
    if request.GET.get('special'):
        low_charachter.extend(list('~!@#$%^&*(){}'))
    if request.GET.get('number'):
        low_charachter.extend(list('0123456789'))
    lenght = int(request.GET.get('lenght', 7))

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(low_charachter)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')
