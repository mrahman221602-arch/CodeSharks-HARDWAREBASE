from django.db import models
from components.models import *

''' Tables:
* Build
* BuildRam
* BuildStorage
'''

class Build(models.Model):

    class AccessChoices(models.TextChoices):
        PRIVATE = 'private', 'Private'
        PUBLIC = 'public', 'Public'

    class StateChoices(models.TextChoices):
        INCOMPLETE = 'incomplete', 'Incomplete'
        COMPLETE = 'complete', 'Complete'

    user = models.ForeignKey()
    name = models.CharField(max_length=50, blank=True)
    create_date = models.DateField(auto_now_add=True)
    access = models.CharField(max_length=10, choices=AccessChoices.choices)
    state = models.CharField(max_length=20, choices=StateChoices.choices)

    cpu = models.ForeignKey(CPU, on_delete=models.SET_NULL, null=True, related_name='cpu_build')
    motherboard = models.ForeignKey(Motherboard, on_delete=models.SET_NULL, null=True, related_name='mb_build')
    gpu = models.ForeignKey(GPU, on_delete=models.SET_NULL, null=True, related_name='gpu_build')
    psu = models.ForeignKey(PSU, on_delete=models.SET_NULL, null=True, related_name='psu_build')
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True, related_name='case_build')

    def __str__(self):
        return f'{self.pk}'
    
# --- Build Junction Tables ---

class BuildRam(models.Model):

    build = models.ForeignKey(Build, on_delete=models.CASCADE, null=True, related_name='included_ram')
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE, null=True, related_name='included_build')
    quantity = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['build', 'ram'], name='unique_build_ram')
        ]

    def __str__(self):
        return f'JTable: BuildRam [{self.build.pk} - {self.ram.name}]'
    
# ---

class BuildStorage(models.Model):

    build = models.ForeignKey(Build, on_delete=models.CASCADE, null=True, related_name='included_storage')
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, null=True, related_name='included_build')
    quantity = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['build', 'storage'], name='unique_build_storage')
        ]

    def __str__(self):
        return f'JTable: BuildStorage [{self.build.pk} - {self.storage.name}]'