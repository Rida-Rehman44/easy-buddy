import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
import jwt
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, UserAuthenticationForm

#######normal user

def landingpage(request):
    return render(request, 'landing_page.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('trip:home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


######################## Google

def sign_in(request):
    return render(request, 'sign_in.html')


@csrf_exempt
def auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    token = request.POST['credential']

    try:
        user_data = id_token.verify_oauth2_token(token, requests.Request(), '685733129857-05vo10qj46jl8it9j87d2pkil45tsv25.apps.googleusercontent.com'
        )
    except ValueError:
        return HttpResponse(status=403)

    # In a real app, I'd also save any new user here to the database.
    # See below for a real example I wrote for Photon Designer.
    # You could also authenticate the user here using the details from Google
    # (https://docs.djangoproject.com/en/4.2/topics/auth/default/#how-to-log-a-user-in)
    request.session['user_data'] = user_data

    return redirect('home')


def sign_out(request):
    del request.session['user_data']
    return redirect('sign_in')


##############calendar changes


def loginview(request):
    context = {}
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                return redirect('trip:home')
        context['form'] = form
    else:
        form = UserAuthenticationForm()
        context['form'] = form

    return render(request, 'login.html', context)


def registerview(request):
    context ={}
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('trip:home')

    else:
        form = RegisterForm()
        context['form'] = form

    return render(request, 'register.html')


def logoutview(request):
    logout(request)
    return redirect('http://localhost:8000/')


