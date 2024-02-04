import math as m
def circle_area(r):
    C = 2 * m.pi * r
    return round(C,2)

def circle_circumference(r):
    A = m.pi * pow(r,2)
    return round(A,2)

r = int(input("Enter circle radius: "))
print("Circle circumference is " , circle_circumference(r))
print("Circle area is " , circle_area(r))
