unique_numbers = []
numbers = [int(x) for x in input("Enter a list of numbers: ").split()]
for i in numbers:
    if i not in unique_numbers:
        unique_numbers.append(i)

unique_numbers.sort(reverse=True)
print(unique_numbers)