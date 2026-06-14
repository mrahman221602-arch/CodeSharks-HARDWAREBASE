from components.models import *

# ---

def calculate_total_price(
        cpu: CPU,
        motherboard: Motherboard,
        ram: RAM,
        storage: Storage,
        gpu: GPU,
        psu: PSU,
        case: Case
):
    total_price = 0

    if cpu: total_price += cpu.price
    if motherboard: total_price += motherboard.price
    if ram: total_price += ram.price
    if storage: total_price += storage.price
    if gpu: total_price += gpu.price
    if psu: total_price += psu.price
    if case: total_price += case.price

    return total_price

# ---

def calculate_total_wattage(cpu: CPU, gpu: GPU):

    total_wattage = 0

    if cpu: total_wattage += cpu.tdp
    if gpu: total_wattage += gpu.tdp

    return total_wattage