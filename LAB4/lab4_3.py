first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

capitalized_first_name = first_name.capitalize() #เพิ่มตรงนี้ให้เรียกจะได้ไม่สับสน

lucky_number = int(len(last_name) / len(capitalized_first_name))

print(f"Hi {capitalized_first_name} {last_name.upper()}, your lucky number is {lucky_number}")
for _ in range(lucky_number):
    print(capitalized_first_name)



#ส่วนของคนที่สอง คิดคล้ายๆกัน แต่ต้องปรับตรงนามสกุลของคนที่สองที่ต้อง
new_first_name = input("Please enter a name to replace your first name: ")
characters_to_strip = input("Please enter characters to be stripped out from your last name: ")

new_full_name = new_first_name.capitalize() + " " + last_name.replace(characters_to_strip, "") #.replace เพื่อstr ที่ต้องการ มันเป็นเมทธอทของpython

new_lucky_number = int(len(last_name.replace(characters_to_strip, "")) / len(new_first_name)) #คิดค่าแบบเดิมคล้ายคนแรกเลย 

print(f"Hi {new_full_name.upper()}, your new lucky number is {new_lucky_number}")
for _ in range(new_lucky_number):
    print(new_first_name)
