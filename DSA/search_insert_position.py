class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        found = False
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                found = True
                return mid
            if nums[mid] < target:
                low = mid+1
            if nums[mid] > target:
                high = mid-1
        if not found:
            for i in range(n):
                if nums[i] > target:
                    return i
            return i+1
