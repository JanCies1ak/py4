def calculate_panels(floor_length, floor_weight, panel_length, panel_weight, panels_in_package):
    floor_area = floor_length * floor_weight * 1.1
    panel_area = panel_length * panel_weight
    return float(floor_area / panel_area / panels_in_package).__ceil__()


print(f"Potrzeba: {calculate_panels(4, 4, 0.2, 1, 10)}")
