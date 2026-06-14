from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from users.models import User
from components.models import *
from .utils import *
from .compatibility import CompatibilityChecker

# ---

def builder_view(req: HttpRequest):

    # get current user info from session
    cuid = req.session.get('cuid')
    if cuid:
        logged_in = True
        user = User.objects.filter(pk=cuid).first()
    else: 
        logged_in = False
        user = None

    # get currently selected component info
    cs_cpu = CPU.objects.filter(pk=req.session.get('cs_cpu', 0)).first()
    cs_mb = Motherboard.objects.filter(pk=req.session.get('cs_mb', 0)).first()
    cs_ram = RAM.objects.filter(pk=req.session.get('cs_ram', 0)).first()
    cs_storage = Storage.objects.filter(pk=req.session.get('cs_storage', 0)).first()
    cs_gpu = GPU.objects.filter(pk=req.session.get('cs_gpu', 0)).first()
    cs_psu = PSU.objects.filter(pk=req.session.get('cs_psu', 0)).first()
    cs_case = Case.objects.filter(pk=req.session.get('cs_case', 0)).first()

    # get total build cost
    total_cost = calculate_total_price(cs_cpu, cs_mb, cs_ram, cs_storage, cs_gpu, cs_psu, cs_case)

    # get total build wattage
    total_wattage = calculate_total_wattage(cs_cpu, cs_gpu)

    # check compatibility
    checker = CompatibilityChecker(cs_cpu, cs_mb, cs_ram, cs_storage, cs_gpu, cs_psu, cs_case)
    hard_inc, soft_inc = checker.check_compatibility()
    can_save = True if not hard_inc else False

    context = {

        # user context
        'logged_in': logged_in,
        'user': user,

        # selected components context
        'cs_cpu': cs_cpu,
        'cs_mb': cs_mb,
        'cs_ram': cs_ram,
        'cs_storage': cs_storage,
        'cs_gpu': cs_gpu,
        'cs_psu': cs_psu,
        'cs_case': cs_case,

        # build stats context
        'tcost': total_cost,
        'twattage': total_wattage,

        # incompatility context
        'hard_inc': hard_inc,
        'soft_inc': soft_inc,
        'can_save': can_save,

    }

    return render(req, 'builder/builder.html', context)

# ---

def start_new_build(req: HttpRequest):

    if 'cs_cpu' in req.session: del req.session['cs_cpu']
    if 'cs_mb' in req.session: del req.session['cs_mb']
    if 'cs_ram' in req.session: del req.session['cs_ram']
    if 'cs_storage' in req.session: del req.session['cs_storage']
    if 'cs_gpu' in req.session: del req.session['cs_gpu']
    if 'cs_psu' in req.session: del req.session['cs_psu']
    if 'cs_case' in req.session: del req.session['cs_case']

    return redirect('builder')

# ---

def component_list(req: HttpRequest, comp: str = None):

    # get current user info from session
    cuid = req.session.get('cuid')
    if cuid:
        logged_in = True
        user = User.objects.filter(pk=cuid).first()
    else: 
        logged_in = False
        user = None
    context = {
        'logged_in': logged_in,
        'user': user,
    }
    # match component type
    match comp:
        case 'cpu':
            context['cpus'] = CPU.objects.all()
            return render(req, 'builder/cpu_select.html', context)
        case 'motherboard':
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

def component_select(req: HttpRequest):

    # get selected component info
    comp = req.GET.get('comp')
    comp_id = int(req.GET.get('id', 0))

    # match component type and update session variable
    match comp:
        case 'cpu':
            req.session['cs_cpu'] = comp_id
        case 'motherboard':
            req.session['cs_mb'] = comp_id
        case 'ram':
            req.session['cs_ram'] = comp_id
        case 'storage':
            req.session['cs_storage'] = comp_id
        case 'gpu':
            req.session['cs_gpu'] = comp_id
        case 'psu':
            req.session['cs_psu'] = comp_id
        case 'case':
            req.session['cs_case'] = comp_id
    
    return redirect('builder')

# ---

def component_remove(req: HttpRequest, comp: str = None):

    # match component type and update session variable
    match comp:
        case 'cpu':
            if 'cs_cpu' in req.session:
                del req.session['cs_cpu']
        case 'motherboard':
            if 'cs_mb' in req.session:
                del req.session['cs_mb']
        case 'ram':
            if 'cs_ram' in req.session:
                del req.session['cs_ram']
        case 'storage':
            if 'cs_storage' in req.session:
                del req.session['cs_storage']
        case 'gpu':
            if 'cs_gpu' in req.session:
                del req.session['cs_gpu']
        case 'psu':
            if 'cs_psu' in req.session:
                del req.session['cs_psu']
        case 'case':
            if 'cs_case' in req.session:
                del req.session['cs_case']

    return redirect('builder')