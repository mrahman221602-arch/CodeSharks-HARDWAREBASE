from django.urls import path
from . import views

# root: localhost:8000/pc-builder/

urlpatterns = [
    path('', views.builder_view, name='builder'),                       # localhost:8000/pc-builder/              
    path('parts/<str:comp>/', views.component_list, name='parts'),      # localhost:8000/pc-builder/parts/<comp>/
    path('select/', views.component_select, name='select'),             # localhost:8000/pc-builder/select/
    path('remove/<str:comp>', views.component_remove, name='remove'),   # localhost:8000/pc-builder/remove/<comp>/
]