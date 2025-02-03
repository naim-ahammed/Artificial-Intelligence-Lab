# • Write a python program to find the sum of the numbers passed as parameters.

def fS(*nums):
    return sum(nums)

nums = input("Enter any numbers: ").split()
nums = [float(num) for num in nums]

tS = fS(*nums)
print("sum of entered numbers: ", tS)