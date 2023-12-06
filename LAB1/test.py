#ข้อ2
price=int(input("Enter product's price :"))
vat=int(input("Enter VAT rate(.0-100) :"))
value=price+(price*vat/100)
print("Total with VAT:",value ,"baht.")
