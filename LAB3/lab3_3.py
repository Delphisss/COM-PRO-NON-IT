product_prices = [float(input(f"Enter product{i + 1}'s price: ")) for i in range(5)]
vat_rate = float(input("Enter VAT rate (0-100): "))
budget = float(input("Enter your budget: "))

total_with_vat = sum(price * (1 + vat_rate / 100) for price in product_prices)
exceeds_budget = total_with_vat > budget

print(f"Total with VAT: {total_with_vat} baht. It exceeds your budget: {exceeds_budget}")
