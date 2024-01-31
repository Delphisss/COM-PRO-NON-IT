def getPricePlusVAT(price, country_code):
    vat_rates = {'TH': 0.07, 'UK': 0.20, 'FI': 0.24, 'SE': 0.25}
    
    if country_code in vat_rates:
        vat_rate = vat_rates[country_code]
        total_price = price * (1 + vat_rate)
        return round(total_price, 2)
    else:
        return -1

country_code = input('Enter country code: ')
total_price = float(input('Enter total price: '))

result = getPricePlusVAT(total_price, country_code)
if result == -1:
    print('No info')
else:
    print(f'Total price with VAT is {result:.2f}')
