def find_smallest(arr):

    minimum = float('inf')
    for num in arr:

        if num < minimum:
            minimum = num

    return minimum

def find_second_smallest(arr):

    minimum = find_smallest(arr)
    second = float('-inf')
    for num in arr:

        if num > minimum:
            second = num

    return second

nums = [12, 25, 8, 55, 10, 33, 17, 11]
print(find_smallest(nums))
print(find_second_smallest(nums))