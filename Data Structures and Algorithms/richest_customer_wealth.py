class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = {}
        for i in range(len(accounts)) :
            wealth[i] = sum(accounts[i])
        return max(wealth.values())