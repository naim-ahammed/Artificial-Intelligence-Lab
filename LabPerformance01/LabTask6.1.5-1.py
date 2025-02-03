# • Write a python program to find the sum of odd and even numbers from a set of numbers.

def EvenOddSum(a, n):
    even = 0
    odd = 0
    for i in range(n):
        if i % 2 == 0:
            even += int(a[i])  
        else:
            odd += int(a[i])   
     
    print("even sum:", even)
    print("odd sum:", odd)

arr = input("Enter any numbers: ").split()
n = len(arr)

EvenOddSum(arr, n)




# num = int(input("enter any number: "))

# if num % 2 == 0:
#     print("even numbers")
# elif num % 2 != 0:
#     print("odd numbers")
# else:
#     print("0 numbers")
    

