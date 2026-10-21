def mergeSort(arr):

    n = len(arr)

    if n <= 1:
        return arr
    
    mid = n//2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1

        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res

nums = [2,5,1,3,4]

max = float("-inf")
second = float("-inf")

for num in nums:

    if num >= max:
        max = num

nums.remove(max)
print(mergeSort(nums))
