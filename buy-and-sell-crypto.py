class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxarr = [0]*n
        maxarr[n-1]=prices[n-1]
        for i in range(len(prices)-2,-1,-1):
            maxarr[i] = max(maxarr[i+1], prices[i])
        res = 0
        for i in range(n-1):
            res = max(res, maxarr[i+1]-prices[i])
        return res


            
        