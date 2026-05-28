class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        map = {}
        majority = 0
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
        for i in map:
            if map[i] > n/2:
                majority = map[i]
                return i