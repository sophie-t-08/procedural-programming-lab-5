a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))

def calculate_area(a, b, c):
    s = (a+b+c)/c
    area = **s(s-a)(s-b)(s-c)
    return area

calculate_area(a, b, c)