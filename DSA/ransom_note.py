class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmapMag = {}
        hashmapRansom = {}
        for c in magazine:
            hashmapMag[c] = hashmapMag.get(c,0)+1
        for c in ransomNote:
            hashmapRansom[c] = hashmapRansom.get(c,0)+1

        for c in ransomNote:

            if c not in hashmapMag:
                return False
                
            if hashmapRansom[c] > hashmapMag[c]:
                return False
        
        return True
        

        
