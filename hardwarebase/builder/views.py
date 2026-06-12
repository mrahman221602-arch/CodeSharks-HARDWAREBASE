from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from users.models import User
from components.models import *

# ---

def builder_view(req: HttpRequest):

    # get current user info from session
    cuid = req.session.get('cuid')
    if cuid:
        user = User.objects.filter(pk=cuid).first()
        context = {
            'logged_in': True,
            'user': user,
        }
        return render(req, 'builder/builder.html', context)

    return render(req, 'builder/builder.html', { 'logged_in': False })

# ---

def component_list(req: HttpRequest, comp: str = None):

    # get current user info from session
    cuid = req.session.get('cuid')
    if cuid:
        logged_in = True
        user = User.objects.filter(pk=cuid).first()
    else: logged_in = False
    context = {
        'logged_in': logged_in,
        'user': user,
    }
    # match component type
    match comp:
        case 'cpu':
            context['cpus'] = CPU.objects.all()
            return render(req, 'builder/cpu_select.html', context)
        case 'mb':
            context['motherboards'] = Motherboard.objects.all()
            return render(req, 'builder/mb_select.html', context)
        case 'ram':
            context['rams'] = RAM.objects.all()
            return render(req, 'builder/ram_select.html', context)
        case 'storage':
            context['storages'] = Storage.objects.all()
            return render(req, 'builder/storage_select.html', context)
        case 'gpu':
            context['gpus'] = GPU.objects.all()
            return render(req, 'builder/gpu_select.html', context)
        case 'psu':
            context['psus'] = PSU.objects.all()
            return render(req, 'builder/psu_select.html', context)
        case 'case':
            context['cases'] = Case.objects.all()
            return render(req, 'builder/case_select.html', context)

# ---

# def cpu_list(req: HttpRequest):
#     cuid = req.session.get('cuid')
#     if cuid:
#         logged_in = True
#         user = User.objects.filter(pk=cuid).first()
#     else: logged_in = False
#     cpus = CPU.objects.all()
#     context = {
#         'logged_in': logged_in,
#         'user': user,
#         'cpus': cpus,
#     }
#     return render(req, 'builder/cpu_select.html', context)

# # ---

# def mb_list(req: HttpRequest):
#     cuid = req.session.get('cuid')
#     if cuid:
#         logged_in = True
#         user = User.objects.filter(pk=cuid).first()
#     else: logged_in = False
#     motherboards = Motherboard.objects.all()
#     context = {
#         'logged_in': logged_in,
#         'user': user,
#         'motherboards': motherboards,
#     }
#     return render(req, 'builder/mb_select.html', context)

# # ---

# def ram_list(req: HttpRequest):
#     cuid = req.session.get('cuid')
#     if cuid:
#         logged_in = True
#         user = User.objects.filter(pk=cuid).first()
#     else: logged_in = False
#     rams = RAM.objects.all()
#     context = {
#         'logged_in': logged_in,
#         'user': user,
#         'rams': rams,
#     }
#     return render(req, 'builder/ram_select.html', context)

# # ---

# def storage_list(req: HttpRequest):
#     cuid = req.session.get('cuid')
#     if cuid:
#         logged_in = True
#         user = User.objects.filter(pk=cuid).first()
#     else: logged_in = False
#     storages = Storage.objects.all()
#     context = {
#         'logged_in': logged_in,
#         'user': user,
#         'storages': storages,
#     }
#     return render(req, 'builder/storage_select.html', context)

# # ---

# def gpu_list(req: HttpRequest):
#     cuid = req.session.get('cuid')
#     if cuid:
#         logged_in = True
#         user = User.objects.filter(pk=cuid).first()
#     else: logged_in = False
#     gpus = GPU.objects.all()
#     context = {
#         'logged_in': logged_in,
#         'user': user,
#         'gpus': gpus,
#     }
#     return render(req, 'builder/gpu_select.html', context)

# # ---

# def psu_list(req: HttpRequest):
#     cuid = req.session.get('cuid')
#     if cuid:
#         logged_in = True
#         user = User.objects.filter(pk=cuid).first()
#     else: logged_in = False
#     psus = PSU.objects.all()
#     context = {
#         'logged_in': logged_in,
#         'user': user,
#         'psus': psus,
#     }
#     return render(req, 'builder/psu_select.html', context)

# # ---

# def case_list(req: HttpRequest):
#     cuid = req.session.get('cuid')
#     if cuid:
#         logged_in = True
#         user = User.objects.filter(pk=cuid).first()
#     else: logged_in = False
#     cases = Case.objects.all()
#     context = {
#         'logged_in': logged_in,
#         'user': user,
#         'cases': cases,
#     }
#     return render(req, 'builder/case_select.html', context)