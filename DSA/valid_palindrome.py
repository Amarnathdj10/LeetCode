class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(char for char in s if char.isalnum()).lower()
        return s1[::-1] == s1