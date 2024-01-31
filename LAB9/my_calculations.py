# my_calculations.py

def working_capital(current_assets, current_liabilities):
    return [a - l for a, l in zip(current_assets, current_liabilities)]

def current_ratio(current_assets, current_liabilities):
    return [round(a / l, 2) for a, l in zip(current_assets, current_liabilities)]

def debt_to_assets(current_liabilities, total_assets):
    return round(sum(current_liabilities) / total_assets, 3)
