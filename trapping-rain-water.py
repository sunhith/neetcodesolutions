class Solution:
    def trap(self, height: List[int]) -> int:
        # Solution-1 
        # Tc - o(n)
        # Sc - o(n)
        """
        n = len(height)
        left_max = [0]*(n)
        right_max = [0]*(n)
        # At certain point it can store water of min(max_left of the point, max_right of the point)
        for i in range(n):
            if i == 0:
                left_max[i] = height[i]
                right_max[n-1-i] = height[n-1-i]
            else:
                left_max[i] = max(left_max[i-1], height[i] )
                right_max[n-1-i] = max(right_max[n-i], height[n-1-i] )
        storage = 0
        for i in range(1,n-1,1):
            min_val = min(left_max[i], right_max[i]) - height[i]
            storage+=min_val
        return storage
"""
        # Solution-2 -> Two Pointer Approach 
        # Tc - o(n)
        # Sc - o(1)
        n = len(height)
        i,j = 0,n-1
        lmax= height[0]
        rmax= height[n-1]
        res = 0
        while(i<j):
            if lmax < rmax:
                res+= lmax-height[i]
                i+=1
                lmax = max(lmax, height[i])
            else:
                res+= rmax-height[j]
                j-=1
                rmax = max(rmax, height[j])
        return res

