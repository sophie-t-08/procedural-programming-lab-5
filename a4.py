temperatures = [12, 15, 18, 21, 19, 16, 14, 11]

def calculate_average(temperatures):
    total = 0
    average_temp = 0
    count = 0
    for i in temperatures:
        total = total + i
        count = count + 1
    average_temp = total/count
    print(average_temp)
def find_highest(temperatures):
    highest_temp = temperatures[0]
    for i in temperatures:
        if i+1 > highest_temp:
            highest_temp = i
    print(highest_temp)
def find_lowest(temperatures):
    for i in temperatures:
        lowest_temp = i
        if i < lowest_temp:
            lowest_temp = i
    print(lowest_temp)
def count_hot_days(temperatures):
    hot_days = 0
    for i in temperatures:
        if i > 20:
            hot_days = hot_days + 1
    print(hot_days)

calculate_average(temperatures)
find_highest(temperatures)
find_lowest(temperatures)
count_hot_days(temperatures)