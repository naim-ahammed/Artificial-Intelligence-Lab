# Set: Find the common elements between two lists using sets.

def FCE(a, b):
    return list(set(a) & set(b))  

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
result = FCE(a, b)
print(result)
