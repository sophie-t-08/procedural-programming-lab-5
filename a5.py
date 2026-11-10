unique_numbers = []
numbers = [int(x) for x in input("Enter a list of numbers: ").split()]

def unique_sorted(numbers):
    unique_numbers = []
    for i in numbers:
        if i not in unique_numbers:
            unique_numbers.append(i)
    unique_numbers.sort(reverse=True)
    return unique_numbers


print(unique_sorted(numbers))