class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        for i in range(len(s)-1):
            if dict1[s[i]] < dict1[s[i+1]]:
                total -= dict1[s[i]]
            else:
                total += dict1[s[i]]
        return total + dict1[s[-1]]