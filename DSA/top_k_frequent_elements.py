class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count frequencies using a hashmap
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # Step 2: Create buckets where the index is the frequency
        # We need len(nums) + 1 so the highest possible frequency fits
        freq = [[] for i in range(len(nums) + 1)]
        for num, c in count.items():
            freq[c].append(num)
            
        # Step 3: Iterate backwards from highest frequency to gather top k
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result