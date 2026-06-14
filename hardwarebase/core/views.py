from django.shortcuts import render, redirect
from django.http import HttpRequest
from users.models import User

# homepage view
def index_view(req: HttpRequest):

    # get current user info from session and render with user context
    cuid = req.session.get('cuid')
    if cuid:
        user = User.objects.filter(pk=cuid).first()
        context = {
            'logged_in': True,
            'user': user,
        }
        return render(req, 'core/index.html', context)

    return render(req, 'core/index.html', { 'logged_in': False })