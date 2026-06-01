from django.db import models

# --- Primary Tables ---

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

class RAM(models.Model):

    class MemTypeChoices(models.TextChoices):
        DDR2 = 'DDR2', 'DDR2'
        DDR3 = 'DDR3', 'DDR3'
        DDR4 = 'DDR4', 'DDR4'
        DDR5 = 'DDR5', 'DDR5'
    
    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=50)
    mem_type = models.CharField(max_length=50, choices=MemTypeChoices.choices)
    form_factor = models.CharField(max_length=50)
    speed = models.IntegerField()
    latency = models.IntegerField()
    timing = models.CharField(max_length=50)
    perf_score = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}'
    
# ---

class Storage(models.Model):

    class TypeChoices(models.TextChoices):
        HDD = 'HDD', 'HDD'
        SSD = 'SSD', 'SSD'
    
    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=50)
    capacity = models.IntegerField()
    storage_type = models.CharField(max_length=50, choices=TypeChoices.choices)
    form_factor = models.CharField(max_length=50)
    cache = models.IntegerField(blank=True, null=True)
    interface = models.CharField(max_length=50)
    is_nvme = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}'
    
# ---

class PSU(models.Model):

    class TypeChoices(models.TextChoices):
        ATX = 'ATX', 'ATX'
        SFX = 'SFX', 'SFX'
        TFX = 'TFX', 'TFX'
    
    class EfficiencyChoices(models.TextChoices):
        STANDARD = '80+ Standard', '80+ Standard'
        BRONZE = '80+ Bronze', '80+ Bronze'
        SILVER = '80+ Silver', '80+ Silver'
        GOLD = '80+ Gold', '80+ Gold'
        PLATINUM = '80+ Platinum', '80+ Platinum'

    class ModularityChoices(models.TextChoices):
        NONMOD = 'Non-Modular', 'Non-Modular'
        SEMIMOD = 'Semi-Modular', 'Semi-Modular'
        FULLMOD = 'Full-Modular', 'Fully Modular'

    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=50)
    psu_type = models.CharField(max_length=10, choices=TypeChoices.choices)
    eff_rating = models.CharField(max_length=50, choices=EfficiencyChoices.choices)
    wattage = models.IntegerField()
    length = models.IntegerField()
    modularity = models.CharField(max_length=50, choices=ModularityChoices.choices)
    is_fanless = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}'
    
# ---

class GPU(models.Model):

    class MemoryTypeChoices(models.TextChoices):
        GDDR5 = 'GDDR5', 'GDDR5'
        GDDR6 = 'GDDR6', 'GDDR6'
        GDDR6X = 'GDDR6X', 'GDDR6X'
        GDDR7 = 'GDDR7', 'GDDR7'

    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=50)
    chipset = models.CharField(max_length=50)
    vram = models.IntegerField()
    vram_type = models.CharField(max_length=50, choices=MemoryTypeChoices.choices)
    core_clk = models.IntegerField()
    boost_clk = models.IntegerField()
    interface = models.CharField(max_length=50)
    length = models.IntegerField()
    tdp = models.IntegerField()
    cooling_fan = models.IntegerField()
    dp_count = models.IntegerField()
    hdmi_count = models.IntegerField()
    perf_score = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}'
    
# ---

class Case(models.Model):

    class SidePanelChoices(models.TextChoices):
        TG = 'Tempered-Glass', 'Tempered Glass'
        SM = 'Solid-Metal', 'Solid Metal'
        AC = 'Acrylic', 'Acrylic'

    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=50)
    case_type = models.CharField(max_length=50)
    side_panel = models.CharField(max_length=50, choices=SidePanelChoices.choices)
    max_gpu_length = models.IntegerField()
    dbay_25_count = models.IntegerField()
    dbay_35_count = models.IntegerField()
    fan_top_count = models.IntegerField()
    fan_rear_count = models.IntegerField()
    fan_mbtray_count = models.IntegerField()
    rad_top_count = models.IntegerField()
    rad_rear_count = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}'
    

    
# --- Junction Tables ---

class CaseMbFormFactor(models.Model):

    class FormFactorChoices(models.TextChoices):
        EATX = 'E-ATX', 'E-ATX'
        ATX = 'ATX', 'ATX'
        MICRO_ATX = 'Micro-ATX', 'Micro-ATX'
        MINI_ITX = 'Mini-ITX', 'Mini-ITX'

    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=True, related_name='related_mb')
    mb_form_factor = models.CharField(max_length=50, choices=FormFactorChoices.choices)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['case', 'mb_form_factor'], name='unique_form_factor')
        ]

    def __str__(self):
        return f'JTable: CaseMbFormFactor [{self.case.name} - {self.mb_form_factor}]'
    
# ---

class CaseFrontPanelUSB(models.Model):

    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=True, related_name='related_usb')
    fpanel_usb = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['case', 'fpanel_usb'], name='unique_fpanel_usb')
        ]

    def __str__(self):
        return f'JTable: CaseFrontPanelUSB [{self.case.name} - {self.fpanel_usb}]'