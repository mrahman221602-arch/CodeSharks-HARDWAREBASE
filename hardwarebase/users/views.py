from django.http import HttpRequest
from django.shortcuts import render
from .forms import UserForm


def signup_view(req: HttpRequest):

    # POST request
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            form.save()
            return render()
        else:
            context = { 'errors': form.errors }
            return render()
  
    # GET request
    return render()


def login_view(req: HttpRequest):

    # POST request
    if req.method == 'POST':

        # session logic
        
        pass

    # GET request
    return render()


def logout_view(req: HttpRequest):
    pass