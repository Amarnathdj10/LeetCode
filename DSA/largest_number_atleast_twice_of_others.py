class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max = 0
        second = 0
        max_index = 0
        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]
                max_index = i

        nums.remove(max)

        for i in range(len(nums)):
            if nums[i] > second:
                second = nums[i]
        if max >= second*2:
            return max_index
        else:
            return -1
