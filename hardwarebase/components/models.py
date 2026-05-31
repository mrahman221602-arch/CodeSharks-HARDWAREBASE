from django.db import models

# ---

class CPU(models.Model):

    class BrandChoices(models.TextChoices):
        AMD = 'AMD', 'AMD'
        INTEL = 'Intel', 'Intel'

    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=50, choices=BrandChoices.choices)
    series = models.CharField(max_length=50)
    microarch = models.CharField(max_length=50)
    socket = models.CharField(max_length=50)
    pcore = models.IntegerField()
    ecore = models.IntegerField(blank=True, null=True)
    thread = models.IntegerField()
    pcore_clk = models.DecimalField(max_digits=4, decimal_places=2)
    pcore_boost = models.DecimalField(max_digits=4, decimal_places=2)
    ecore_clk = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ecore_boost = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    l2cache = models.IntegerField()
    l3cache = models.IntegerField()
    tdp = models.IntegerField()
    igpu = models.CharField(max_length=50, blank=True)
    max_mem = models.IntegerField()
    lithography = models.IntegerField()
    perf_score = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}'
    
# ---

class Motherboard(models.Model):

    class FormFactorChoices(models.TextChoices):
        EATX = 'E-ATX', 'E-ATX'
        ATX = 'ATX', 'ATX'
        MICRO_ATX = 'Micro-ATX', 'Micro-ATX'
        MINI_ITX = 'Mini-ITX', 'Mini-ITX'

    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=50)
    socket = models.CharField(max_length=50)
    form_factor = models.CharField(max_length=50, choices=FormFactorChoices.choices)
    chipset = models.CharField(max_length=50)
    max_mem = models.IntegerField()
    mem_type = models.CharField(max_length=50)
    mem_slot = models.IntegerField()
    mem_speed = models.IntegerField()
    pcie_slot = models.IntegerField()
    m2_slot = models.IntegerField()
    sata_port = models.IntegerField()
    usb2_header = models.IntegerField()
    usb3_header = models.IntegerField()
    wireless = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}'
    
# ---