from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from .models import User
from .forms import *


def signup_view(req: HttpRequest):
    
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['pwd_hash']
        
            # username and email validation
            if User.objects.filter(Q(username=username) | Q(email=email)).exists():
                return render(req, '')
            
            # create password hash for storage
            p_hash = make_password(password)

            # create new user record
            User.objects.create(username=username, email=email, pwd_hash=p_hash)

            return redirect('login')
    
    return render(req, '')


def login_view(req: HttpRequest):
    
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            user_id = form.cleaned_data['userid']
            password = form.cleaned_data['password']

            # userid field validation
            if User.objects.filter(username=user_id).exists():
                user = User.objects.get(username=user_id)
            elif User.objects.filter(email=user_id).exists():
                user = User.objects.get(email=user_id)
            else:
                return render(req, '')

            # password field validation
            if not check_password(password, user.pwd_hash):
                return render(req, '')
            
            # set CUID in session
            req.session['cuid'] = user.pk
            return render(req, '')

    return render(req, 'users/login.html')


def logout_view(req: HttpRequest):
    pass