class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution - 1 -> TC=O(n), SC=O(n) -> find the max price that we can sell at a given buy price.
        # So maintain an maxarr -> that contains max value from back side of an array 
        """ 
        n = len(prices)
        maxarr = [0]*n
        maxarr[n-1]=prices[n-1]
        for i in range(len(prices)-2,-1,-1):
            maxarr[i] = max(maxarr[i+1], prices[i])
        res = 0
        for i in range(n-1):
            res = max(res, maxarr[i+1]-prices[i])
        return res
        """
        # Solution - 2 -> TC= O(n), SC= O(1) -> Maintain 2 pointers 1 points to buy price(b) and other to sell price(s)
        # so check for if there are any low sell prices(s) for a given b. In the process if you find any s less than b 
        # move b pointer to s as you found less buy price than b so in future you might get higher sell price then this 
        # buy price would be appropriate.
        # Two pointer Approach - Window Technique
        """
        n = len(prices)
        b,s = 0,1
        res = 0
        while b < n-1 and s < n:
            if prices[b] < prices[s]:
                res = max(res, prices[s]-prices[b])
            else:
                b = s
            s+=1
        return res
        """

        # Solution - 3 -> TC= O(n), SC= O(1) -> DP Approach -> At some point to sell, find the min left in array which is a buy
        # therefore, find max of (sell - min left which is a buy)
        n = len(prices)
        maxProfit = 0
        minBuy = prices[0]
        for sell in prices:
            maxProfit = max(maxProfit, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxProfit


        