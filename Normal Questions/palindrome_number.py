class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = str(x)[::-1]
        return True if rev == str(x) else False