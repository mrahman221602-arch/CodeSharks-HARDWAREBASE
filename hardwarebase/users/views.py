from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .forms import *

# ---

def signup_view(req: HttpRequest):

    signup_errors = {
        'cred_exists': 'Username or email already exists.'
    }
    
    # POST request processing
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['pwd_hash']
            
            # create password hash for storage
            p_hash = make_password(password)

            # create new user record
            User.objects.create(username=username, email=email, pwd_hash=p_hash)

            # redirect to login page
            return redirect('login')

        else: return render(req, 'users/signup.html', {
                'cred_error': signup_errors['cred_exists']
            })
    
    # GET request processing
    return render(req, 'users/signup.html')

# ---

def login_view(req: HttpRequest):

    login_errors = {
        'invalid_cred': 'Invalid credentials. Please try again.'
    }
    
    # POST request processing
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
                return render(req, 'users/login.html', { 
                    'auth_error': login_errors['invalid_cred'] 
                    })

            # password field validation
            if not check_password(password, user.pwd_hash):
                return render(req, 'users/login.html', {
                    'auth_error': login_errors['invalid_cred']
                })
            
            # set CUID in session
            req.session['cuid'] = user.pk
            return render(req, '')

    # GET request processing
    return render(req, 'users/login.html')

# ---

def logout_view(req: HttpRequest):
    pass