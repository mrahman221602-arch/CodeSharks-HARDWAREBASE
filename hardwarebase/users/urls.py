from django.urls import path
from . import views

# root: localhost:8000/users/

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),      # localhost:8000/users/signup/
    path('login/', views.login_view, name='login'),         # localhost:8000/users/login/
    path('logout/', views.logout_view, name='logout'),      # localhost:8000/users/logout/
]