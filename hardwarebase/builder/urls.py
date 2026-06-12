from django.urls import path
from . import views

# root: localhost:8000/pc-builder/

urlpatterns = [
    
    path('', views.builder_view, name='builder'),                   # localhost:8000/pc-builder/              
    # path('cpus/', views.cpu_list, name='cpus'),                     # localhost:8000/pc-builder/cpus/
    # path('motherboards/', views.mb_list, name='motherboards'),      # localhost:8000/pc-builder/motherboards/
    # path('rams/', views.ram_list, name='rams'),                     # localhost:8000/pc-builder/rams/
    # path('storages/', views.storage_list, name='storages'),         # localhost:8000/pc-builder/storages/
    # path('gpus/', views.gpu_list, name='gpus'),                     # localhost:8000/pc-builder/gpus/
    # path('psus/', views.psu_list, name='psus'),                     # localhost:8000/pc-builder/psus/
    # path('cases/', views.case_list, name='cases'),                  # localhost:8000/pc-builder/cases
    path('parts/<str:comp>/', views.component_list, name='parts'),  # localhost:8000/pc-builder/parts/<comp>/
]