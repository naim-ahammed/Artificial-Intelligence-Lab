# List: Given a list of numbers, remove duplicates and sort in ascending order.

def RDS(lst):
    return sorted(set(lst))

numbers = [5, 3, 8, 3, 1, 5, 7, 8, 2]
result = RDS(numbers)
print(result)