# Get user input for first and last names
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

capitalized_first_name = first_name.capitalize()

lucky_number = int(len(last_name) / len(capitalized_first_name))
print(f"Hi {capitalized_first_name} {last_name.upper()}, your lucky number is {lucky_number}")

for _ in range(lucky_number):
    print(capitalized_first_name)
