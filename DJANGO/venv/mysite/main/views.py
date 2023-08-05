from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    data = {
        'title':'Главная', # подключаем словарь данных
        'values': ['123', 'abc','_=_'],
        'obj':{'name':'John Doe','age':'33'}
    }
    return render(request, 'main/index.html', data) # подключаем документ

def about(request):
    return render(request, 'main/about.html',{'title': 'О нас'})


# def about(request):
#     return HttpResponse("<h3>About page !</h3>") # можно небольшой кусочек кода
