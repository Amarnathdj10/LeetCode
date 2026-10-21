def selectionSort(arr):

    n = len(arr)
    for i in range(n):
        minIndex = i

        for j in range(i+1,n):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i],arr[minIndex] = arr[minIndex],arr[i]

    return arr


nums = [2,5,1,3,4]
print(selectionSort(nums))