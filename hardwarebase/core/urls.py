from django.urls import path
from . import views

# root: localhost:8000/

urlpatterns = [
    path('', views.index_view, name='home'),    # localhost:8000/
]