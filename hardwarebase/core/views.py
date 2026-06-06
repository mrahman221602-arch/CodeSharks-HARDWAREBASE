from django.shortcuts import render, redirect
from django.http import HttpRequest

# homepage view
def index_view(req: HttpRequest):
    return render(req, 'core/index.html')