from django.contrib import admin
from .models import *

admin.site.register(Build)
admin.site.register(BuildRam)
admin.site.register(BuildStorage)