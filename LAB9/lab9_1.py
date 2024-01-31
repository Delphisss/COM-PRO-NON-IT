# main_program.py
from my_calculations import working_capital, current_ratio, debt_to_assets

current_assets = [110, 90, 95, 82, 76, 94, 120, 109, 98, 96]
current_liabilities = [180, 92, 91, 80, 82, 83, 85, 90, 91, 92]

# Calculate Working Capital
wc = working_capital(current_assets, current_liabilities)
print(f'Working Capital: {wc}')

# Calculate Current Ratio
cr = current_ratio(current_assets, current_liabilities)
print(f'Current Ratio: {cr}')

# Assume Total Assets is the sum of Current Assets for this example
total_assets = sum(current_assets)

# Calculate Debt to Assets
dta = debt_to_assets(current_liabilities, total_assets)
print(f'Debt to Assets: {dta}')
