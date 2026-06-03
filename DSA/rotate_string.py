class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        doubled = s+s
        return len(s)==len(goal) and goal in doubled