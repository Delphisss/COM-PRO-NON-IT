principal = float(input("Principal: ")) #เงินต้น
annual_interest_rate = float(input("Annual rate: ")) #ดอกเบี้ยต่อปี
num_payments = int(input("Number of payments: ")) #กี่งวด
monthly_interest_rate = (annual_interest_rate / 100) / 12 #คำนวรดอกเบี้ยรายเดือน
monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments) #สูครตามอาจารย์ให้มา

print(f"Monthly payment is {monthly_payment:.2f}") 
