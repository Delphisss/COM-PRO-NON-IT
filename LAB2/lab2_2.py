p = float(input("Principal: ")) #เงินต้น
a = float(input("Annual rate: ")) #ดอกเบี้ยต่อปี
n = int(input("Number of payments: ")) #กี่งวด
monthly_interest_rate = (a / 100) / 12 #คำนวรดอกเบี้ยรายเดือน
monthly_payment = (p * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -n) #สูครตามอาจารย์ให้มา

print(f"Monthly payment is {monthly_payment:.2f}") 
   