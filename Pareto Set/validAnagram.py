class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashmap_s = {}
        hashmap_t = {}

        for c in s:
            hashmap_s[c] = hashmap_s.get(c,0) + 1
        
        for c in t:
            hashmap_t[c] = hashmap_t.get(c,0) + 1
        
        return hashmap_s == hashmap_t