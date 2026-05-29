class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j]%2 != 0:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        return nums