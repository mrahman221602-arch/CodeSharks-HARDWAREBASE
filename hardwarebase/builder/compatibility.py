from components.models import *
from .utils import calculate_total_wattage

# ---

class CompatibilityChecker:

    def __init__(
            self,
            cpu: CPU,
            motherboard: Motherboard,
            ram: RAM,
            storage: Storage,
            gpu: GPU,
            psu: PSU,
            case: Case
    ):
        self.cpu = cpu
        self.motherboard = motherboard
        self.ram = ram
        self.storage = storage
        self.gpu = gpu
        self.psu = psu
        self.case = case

        self.hard_inc = []
        self.soft_inc = []

    def check_compatibility(self):
        self.essential_components()
        self.cpu_mb_socket()
        self.ram_mb_type()
        self.storage_mb_slot()
        self.gpu_mb_slot()
        self.gpu_case_length()

        return self.hard_inc, self.soft_inc

    # ---

    def essential_components(self):
        if not self.cpu or not self.motherboard or not self.ram or not self.storage or not self.psu:
            self.hard_inc.append('Your build is missing essential components')
    
    def cpu_mb_socket(self):
        if self.cpu and self.motherboard:
            if self.cpu.socket != self.motherboard.socket:
                self.hard_inc.append('Motherboard socket is incompatible with CPU')
    
    def ram_mb_type(self):
        if self.ram and self.motherboard:
            if self.ram.mem_type != self.motherboard.mem_type:
                self.hard_inc.append('Mismatched memory types for motherboard and RAM')

    def storage_mb_slot(self):
        if self.storage and self.motherboard:
            if self.storage.is_nvme and self.motherboard.m2_slot < 1:
                self.soft_inc.append('No M.2 slot available for NVMe drive')
            elif not self.storage.is_nvme and self.motherboard.sata_port < 1:
                self.soft_inc.append('No SATA port available for SATA drive')

    def gpu_mb_slot(self):
        if self.gpu and self.motherboard:
            if self.motherboard.pcie_slot < 1:
                self.hard_inc.append('No PCIe slot available for graphics card')
    
    def gpu_case_length(self):
        if self.gpu and self.case:
            if self.gpu.length > self.case.max_gpu_length:
                self.hard_inc.append('Case length is too short for graphics card')
    
    def psu_wattage(self):
        if self.psu and self.cpu and self.gpu:
            tw = calculate_total_wattage(self.cpu, self.gpu)
            if self.psu.wattage < tw:
                self.hard_inc.append('Power supply is inadequate for build')