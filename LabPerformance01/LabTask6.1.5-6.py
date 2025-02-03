# • Write a python program to generate Fibonacci series.

num = int(input("enter any number: "))
a = 0
b = 1
temp = 0
fS = [a, b]

for x in range(num - 2):
    temp = a
    a = b
    b = temp + b
    fS.append(b)

print("fibonacci series:", fS)