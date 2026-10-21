def quickSort(arr):

    n = len(arr)
    if n <= 1:
        return arr

    pivot = arr[-1]

    left, right = [], []
    for x in arr[:-1]:

        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quickSort(left) + [pivot] + quickSort(right)

nums = [2,5,1,3,4]
print(quickSort(nums))