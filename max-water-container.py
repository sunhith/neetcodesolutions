class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0, len(heights)-1
        res = 0
        while i<j:
            area = (j-i)*min(heights[i] , heights[j])
            if heights[i] < heights[j]:   
                i+=1
            elif heights[i] > heights[j]:
                j-=1
            else:
                i+=1
                j-=1
            res = max(area,res)
        return res

        