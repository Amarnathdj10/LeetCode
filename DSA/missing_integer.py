class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0,100000):
            if i not in nums:
                return i