distance = float(input("Enter journey distance in miles: "))
mpg = float(input("Enter car fuel efficiency in MPG: "))
price_per_litre = float(input("Enter price of petrol per litre: "))

def calculate_fuel_cost(distance, mpg, price_per_litre):
    fuel_cost = (distance/mpg)*4.546*price_per_litre
    rounded = round(fuel_cost, 2)
    print(rounded)

calculate_fuel_cost(distance, mpg, price_per_litre)