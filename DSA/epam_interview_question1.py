'''
You are given an array:
[0, 1, 0, 4, 2, 14, 5, 1, 4]

Some elements appear multiple times and some appear only once.
✅ Task:
1. Take elements that occur more than once and sort them in ascending order with their original frequency
2. Take elements that occur only once and sort them in ascending order

Final output (repeated first, then unique):
[0, 0, 1, 1, 4, 4, 2, 5, 14]

'''

'''
arr = [0, 1, 0, 4, 2, 14, 5, 1, 4]
hashmap = {}

for num in arr:

    hashmap[num] = hashmap.get(num,0) + 1 #finds frequency of each number

freq_list = sorted([key for key, freq in hashmap.items()])

pointer = 0

for num in freq_list:
    if hashmap[num] > 1:
        for _ in range(hashmap[num]):

            arr[pointer] = num
            pointer += 1

for num in freq_list:
    if hashmap[num] == 1:
        for _ in range(hashmap[num]):

            arr[pointer] = num
            pointer += 1

print(arr)
'''

'''👉 Modification of this problem was also asked:
Do not sort the elements that appear only once.
Keep them in the same order as they appear in the array.

✅ Modified Output
[0, 0, 1, 1, 4, 4, 2, 14, 5]
'''

arr = [0, 1, 0, 4, 2, 14, 5, 1, 4]
hashmap = {}

for num in arr:

    hashmap[num] = hashmap.get(num,0) + 1 #finds frequency of each number

repeated = sorted([key for key, freq in hashmap.items() if freq > 1])
unique = [key for key, freq in hashmap.items() if freq == 1]

pointer = 0

for num in repeated:
    for _ in range(hashmap[num]):

        arr[pointer] = num
        pointer += 1

for num in unique:
    arr[pointer] = num
    pointer += 1

print(arr)