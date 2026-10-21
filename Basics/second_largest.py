nums = [2,5,1,3,4]

max = float("-inf")
second = float("-inf")

for num in nums:

    if num >= max:
        second = max
        max = num

    elif num > second and num < max:
        second = num

print(second)