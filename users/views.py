import random

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from users.forms import UserLoginForm, UserRegisterForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        print('check')
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                print('all good')
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def generate_code():
    random.seed()
    return str(random.randint(10000, 99999))
# Create your views here.
