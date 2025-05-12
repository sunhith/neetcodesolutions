class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        res = nums[0]
        s = 0
        while r<= len(nums)-1:
            s = s + nums[r]
            res = max(res,s)
            if s <0:
                l = r+1
                r = r+1
                s = 0
            else:
                r = r+1
        return res
        