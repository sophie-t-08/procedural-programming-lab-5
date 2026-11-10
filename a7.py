list1 = [int(x) for x in input("Enter a list of numbers: ").split()]
list2 = [int(x) for x in input("Enter a list of numbers: ").split()]

def max_difference(list1, list2):
    for i in list1:
        largest=max(list1)
        smallest=min(list2)
        difference=largest-smallest
    return difference

print(max_difference(list1, list2))