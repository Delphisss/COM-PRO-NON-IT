score = int(input("Enter the score: ")) 
if 0 <= score <= 100:
        if score >= 80:
            print("Grade: A")
        elif score >= 70:
            print("Grade: B")
        elif score >= 60:
            print("Grade: C")
        elif score >=50:
            print("Grade: D")
        else:
            print("Grade: F")
else:
    print("Error: Score in not within the range 0-100.")