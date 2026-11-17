class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        hashmap = defaultdict(int)

        for i in range(1,n+1):
            
            num = i
            total = 0

            while i > 0:
                
                rem = i%10
                total = total + rem
                i = i//10

            hashmap[total] += 1
        
        maxSize = max(hashmap.values())
        largestGroup = 0

        for size in hashmap.values():

            if size == maxSize:
                largestGroup += 1

        return largestGroup