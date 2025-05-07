class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        k = r
        while l<=r:
            mid = (l+r)//2
            res = 0
            for i in range(len(piles)):
                res+= math.ceil(piles[i]/mid)
                
            if res > h:
                l = mid + 1
            else:
                k=mid
                r = mid - 1
        return k


        