class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        left = 1
        right = max(piles)

        res = right

        while left <= right:
            
            k = (left + right)//2
            hours_spent = 0

            for pile in piles:
                hours_spent += -(-pile//k)
            
            if hours_spent <= h:
                res = k
                right = k-1
            else:
                left = k+1
        
        return res