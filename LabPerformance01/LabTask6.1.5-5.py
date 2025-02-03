# • Write a python program to find the factorial of a number using for loop.

num = int(input("enter any number: "))
f = 1

for i in range(1, num + 1):
    f *= i
print("factorial = ", f)