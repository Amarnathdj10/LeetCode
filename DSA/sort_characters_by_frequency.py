class Solution:
    def frequencySort(self, s: str) -> str:

        hashmap = {}
        res = []

        for c in s:
            hashmap[c] = hashmap.get(c,0) + 1
        
        sorted_map = dict(sorted(hashmap.items(), key = lambda x: x[1], reverse = True))

        for key,value in sorted_map.items():
            res.append(key*value)
        
        s2 = "".join(res)
        return s2