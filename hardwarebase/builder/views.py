from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from users.models import User

# ---

def builder_view(req: HttpRequest):

    # get current user info from session
    cuid = req.session.get('cuid')
    user = User.objects.filter(pk=cuid).first()

    context = {
        'user': user,
    }

    return render(req, 'builder/builder.html', context)