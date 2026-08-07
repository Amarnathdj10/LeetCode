class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        currSum = nums[0]
        for i in range(1,len(nums)):
            currSum += nums[i]
            nums[i] = currSum
        return nums