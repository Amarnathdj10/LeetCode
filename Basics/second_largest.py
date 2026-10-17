class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        max = float('-inf')
        second = float('-inf')
        
        arr_set = set(arr)
        for num in arr_set:
            if num > max:
                max = num

        arr_set.remove(max)

        if len(arr_set) == 0:
            return -1
    
        for num in arr_set:
            if num > second:
                second = num
        return second
        
        