from django.contrib import admin
from .models import *

admin.site.register(CPU)
admin.site.register(Motherboard)
admin.site.register(RAM)
admin.site.register(Storage)
admin.site.register(PSU)
admin.site.register(GPU)
admin.site.register(Case)
admin.site.register(CaseMbFormFactor)
admin.site.register(CaseFrontPanelUSB)