print("Program to check if num1 is in [0-9] and num2 is in [10-99].")
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

correct_num1 = 0 <= num1 <= 9
correct_num2 = 10 <= num2 <= 99

if correct_num1 and correct_num2:
    print("Both numbers are entered correctly.")
elif correct_num1:
    print("Only num1 is entered correctly.")
elif correct_num2:
    print("Only num2 is entered correctly.")
else:
    print("Both numbers are NOT entered correctly.")
print("Goodbye.")

score = int(input("Enter the score: "))

if 0 <= score <= 100:
    if score >= 80:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    elif score >= 60:
        print("Grade: C")
    elif score >= 50:
        print("Grade: D")
    else:
        print("Grade: F")
else:
    print("Error: Score is not within the range 0-100.")
