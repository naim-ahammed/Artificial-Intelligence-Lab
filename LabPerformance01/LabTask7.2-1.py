# • Write a python program to find the largest number between two numbers using function

a = float(input("enter the first number: "))
b = float(input("enter the second number: "))

def fL(a, b):
    if a > b:
        return a
    else:
        return b

larg = fL(a, b)
print("largest number: ", larg)