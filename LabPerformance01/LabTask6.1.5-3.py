# • Write a python program to find the sum of all numbers between 50 and 100, which are divisible by 3 and not divisible by 5.

sum = 0
for n in range(50, 101):
    if (n % 3 == 0 and n % 5 != 0):
        sum+=n 
print("sum of numbers:", sum)