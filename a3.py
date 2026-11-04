import math

a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))

def calculate_area(a, b, c):
    s = (a+b+c)/2
    area = math.sqrt(s*((s-a)*(s-b)*(s-c)))
    print(area)

calculate_area(a, b, c)