class Solution:
    def missingRanges(self, arr, lower, upper):
        
        n = len(arr)
        
        if n==0:
            return [[lower,upper]]
        
        res = []
        
        if lower < arr[0]:
            res.append([lower, arr[0]-1])
        
        for i in range(n-1):
            if arr[i+1] - arr[i] > 1:
                res.append([arr[i]+1, arr[i+1]-1])
            
        if upper > arr[-1]:
            res.append([arr[-1]+1, upper])
            
        return res