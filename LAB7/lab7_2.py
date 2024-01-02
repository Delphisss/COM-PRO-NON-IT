password = "1234"
psw = input("Enter a password: ")
i = 1
while psw != password:
    if(i%3 == 0):
        print("Your've exceeded the number of password attempts.")
    else:
        print("Wrong password. Try again.")
    print()
    psw = input("Enter a password: ")
    i += 1

print("Welcome to our system.") 