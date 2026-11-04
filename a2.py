distance = int(input("Enter journey distance in miles: "))
mpg = int(input("Enter car fuel efficiency in MPG: "))
price_per_litre = int(input("Enter price of petrol per litre: "))

def calculate_fuel_cost(distance, mpg, price_per_litre):
    fuel_cost = (distance/mpg)*4.546*price_per_litre
    return fuel_cost

calculate_fuel_cost(distance, mpg, price_per_litre)