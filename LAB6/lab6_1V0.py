print("Program to check if num1 is in [0-9] and num2 is in [10-99].")
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

num1_correct = num1 >= 0 and num1 <= 9
num2_correct = num2 >= 10 and num2 <= 99

if num1_correct and num2_correct:
    print("Both numbers are entered correctly.")
elif num1_correct:
    print("Only num1 is entered correctly.")
elif num2_correct:
    print("Only num2 is entered correctly.")
else:
    print("Both numbers are NOT entered correctly.")

print("Good bye.")
