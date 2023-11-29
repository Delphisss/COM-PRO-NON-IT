product_price = float(input("Enter product’s price: "))
vat_rate = float(input("Enter VAT rate (0-100): "))
total_with_vat = product_price * (1 + vat_rate / 100)
print(f"Total with VAT: {total_with_vat} baht.")


