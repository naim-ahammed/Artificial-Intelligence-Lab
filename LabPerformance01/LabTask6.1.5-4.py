# • Write a python program to find the second highest number from a set of numbers.

nums = list(map(int, input("enter numbers: ").split()))
uniqNum = set(nums)

h = sH = None
for num in uniqNum:
    if h is None or num > h:
        sH = h
        h = num
    elif sH is None or num > sH:
        sH = num

if sH is not None:
    print("second highest number: ", sH)
else:
    print("not enough numbers")