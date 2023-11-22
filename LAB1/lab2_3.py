#รับเกรดและหน่วยกิต
subject1_grade = float(input("Subject 1 grade (0-4): ")) 
subject1_credits = int(input("Subject 1 credits: "))
subject2_grade = float(input("Subject 2 grade (0-4): "))
subject2_credits = int(input("Subject 2 credits: "))
subject3_grade = float(input("Subject 3 grade (0-4): "))
subject3_credits = int(input("Subject 3 credits: "))

#คำนวณตามสูตร
total_credits = subject1_credits + subject2_credits + subject3_credits 
weighted_sum = (subject1_grade * subject1_credits) + (subject2_grade * subject2_credits) + (subject3_grade * subject3_credits)
gpa = weighted_sum / total_credits


print(f"GPA = {gpa:.1f}")
