# main.py
import my_calculations

current_assets = [110, 90, 95, 82, 76, 94, 120, 109, 98, 96]
current_liabilities = [180, 92, 91, 80, 82, 83, 85, 90, 91, 92]

# Calculate Working Capital
working_capital_result = my_calculations.working_capital(current_assets, current_liabilities)
print("Working Capital:", working_capital_result)

# Calculate Current Ratio
current_ratio_result = my_calculations.current_ratio(current_assets, current_liabilities)
print("Current Ratio:", current_ratio_result)

# Calculate Debt to Assets
debt_assets_result = my_calculations.debt_assets(current_assets, current_liabilities)
print("Debt to Assets:", debt_assets_result)
 