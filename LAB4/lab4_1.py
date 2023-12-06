# def calculate_lucky_number(first_name, last_name):
#     lucky_number = len(last_name) / len(first_name)
#     print(f"Hi {first_name.capitalize()} {last_name.upper()}, your lucky number is {int(lucky_number)}")

# first_name = input("Please enter your first name: ")
# last_name = input("Please enter your last name: ")

# calculate_lucky_number(first_name, last_name)

#อันบนทำเป็นฟังก์ชัั่นอันล่างเขียนตรงๆ


first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
lucky_number = len(last_name) / len(first_name)
print(f"Hi {first_name.capitalize()} {last_name.upper()}, your lucky number is {int(lucky_number)}")

