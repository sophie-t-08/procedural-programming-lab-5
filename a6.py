unique_numbers = []
numbers = [int(x) for x in input("Enter a list of numbers: ").split()]

def contains_duplicates(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False

print(contains_duplicates(numbers))