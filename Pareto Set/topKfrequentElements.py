class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        count = {}
        freq = [[] for _ in range(len(nums)+1)]
        res = []

        for num in nums:
            count[num] = count.get(num,0) + 1
        
        for index, key in count.items():
            freq[key].append(index)
            
        for i in range(len(freq)-1,0,-1):

            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
            


        