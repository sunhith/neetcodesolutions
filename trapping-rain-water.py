class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0]*(n)
        right_max = [0]*(n)
        
        for i in range(n):
            if i == 0:
                left_max[i] = height[i]
                right_max[i] = height[n-1-i]
            else:
                left_max[i] = max(left_max[i-1], height[i] )
                right_max[n-1-i] = max(right_max[n-i], height[n-1-i] )
        storage = 0
        for i in range(1,n-1,1):
            min_val = min(left_max[i-1], right_max[i+1]) - height[i]
            if min_val > 0:
                storage+=min_val
        return storage

