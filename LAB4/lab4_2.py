#เอาlab4_1.py มาโมใหม่
first_name = input("Please enter your first name: ") #รับชื่อ
last_name = input("Please enter your last name: ")  #รับนามสกุล

lucky_number = int(len(last_name) / len(first_name)) 
print(f"Hi {first_name.capitalize()} {last_name.upper()}, your lucky number is {lucky_number}")

print(first_name.capitalize()*lucky_number)
