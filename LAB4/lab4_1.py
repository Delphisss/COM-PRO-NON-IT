# def calculate_lucky_number(first_name, last_name):
#     lucky_number = len(last_name) / len(first_name)
#     print(f"Hi {first_name.capitalize()} {last_name.upper()}, your lucky number is {int(lucky_number)}")

# first_name = input("Please enter your first name: ")
# last_name = input("Please enter your last name: ")

# calculate_lucky_number(first_name, last_name)

#อันบนทำเป็นฟังก์ชัั่นอันล่างเขียนตรงๆ
#เขียนแบบไม่เป็นฟังก์ชั่นก่อน เพราะเนื้อหาของ acc-ba ยังไม่ถึง


first_name = input("Please enter your first name: ") #รับชื่อ
last_name = input("Please enter your last name: ") #รับนามสกุล    
lucky_number = len(last_name) / len(first_name) #นำค่ามาหารหาค่า luck number ตอนแสดงเอาเป็น int
print(f"Hi {first_name.capitalize()} {last_name.upper()}, your lucky number is {int(lucky_number)}") #ปริ้นค่าออกมาตามโจทย์เลย

