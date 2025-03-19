        for i in range(len(nums)-1,-1, -1):
            if i == len(nums)-1:
                prod[i] = prod[i-1] * nums[i]
        
                prod[i] = nums[i]
            else:
        for i in range(len(nums)):
            if i == 0:
        rev_prod = [0] * n  # Initialize with correct size
        res = [0] * n  # Initialize with correct size
        n = len(nums)
        prod = [0] * n  # Initialize with correct size
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

                rev_prod[i] = nums[i]
                rev_prod[i] = rev_prod[i+1]*nums[i]
                res[i] = rev_prod[1]
            elif i == len(nums)-1:
                res[i] = prod[i-1]
                res[i] = prod[i-1]*rev_prod[i+1]
        return res