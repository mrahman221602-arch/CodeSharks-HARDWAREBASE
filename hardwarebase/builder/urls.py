from django.urls import path
from . import views

# root: localhost:8000/pc-builder/

urlpatterns = [
    path('', views.builder_view, name='builder'),      # localhost:8000/pc-builder/
]