class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        hashmap = {']':'[', '}':'{', ')':'('}

        for c in s:
            if c in hashmap:
                top_element = stack.pop() if stack else '#'
                if hashmap[c] != top_element:
                    return False
            else:
                stack.append(c)
        return True