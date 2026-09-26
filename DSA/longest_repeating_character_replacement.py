class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charCounts = {}
        left = 0
        maxLength = 0
        maxFreq = 0
        
        for right in range(len(s)):
            currentChar = s[right]

            charCounts[currentChar] = charCounts.get(currentChar,0) + 1
            maxFreq = max(maxFreq,charCounts[currentChar])

            if (right-left+1) - maxFreq > k:
                charCounts[s[left]] -= 1
                left += 1   

            maxLength = right - left + 1

        return maxLength