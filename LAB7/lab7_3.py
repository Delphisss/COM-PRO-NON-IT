ans = "Y"
while ans == "Y":
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    print("x%y = {}".format(x%y))
    ans = input("Would you like to continue? (Y/N): ")
    while ans != "Y" and ans != "N":
          ans = input("Would you like to continue? (Y/N): ")
print("End of program")