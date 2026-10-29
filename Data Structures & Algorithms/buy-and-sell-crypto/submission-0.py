class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        for i in range(len(prices)):
            for j in prices[:i:-1]:
                p=max(p,j-prices[i])
        return p