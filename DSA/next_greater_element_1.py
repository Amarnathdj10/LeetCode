class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        stack = [] 
        nextGreater = {}

        for num in nums2:

            while stack and stack[-1] < num:
                smaller = stack.pop()
                nextGreater[smaller] = num
            
            stack.append(num)

        for num in stack:
            nextGreater[num] = -1
        
        return [nextGreater[num] for num in nums1]