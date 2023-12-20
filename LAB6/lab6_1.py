# Example 5: A program that checks if the input numbers meet the criteria.
print("Program to check if num1 is in [0-9] and num2 is in [10-99].")
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
if num1 >= 0 and num1 <= 9:
    if num2 >= 10 and num2 <= 99:
print("Both numbers are entered correctly.")
    else:
print("Only num1 is entered correctly.")
else:
    if num2 >= 10 and num2 <= 99:
print("Only num2 is entered correctly.")
    else:
    print("Both numbers are NOT entered correctly.")
print("Good bye.")


# 1) Re-do Example 5 by using a different approach (not nested if).
# 2) Write a program that takes an integer score as an input and gives a corresponding letter grade 
# (see table below). If the score is not within 0-100, print “Error”. You must use if-else-if structure.
# Score Grade
# 80-100 A
# 70-79 B
# 60-69 C
# 50-59 D
# 0-49 F
# Not in the range 0-100 Erro