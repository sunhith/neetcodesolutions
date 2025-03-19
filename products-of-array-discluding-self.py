class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = [0] * n  # Initialize with correct size
        rev_prod = [0] * n  # Initialize with correct size
        res = [0] * n  # Initialize with correct size
        for i in range(len(nums)):
            if i == 0:
                prod[i] = nums[i]
            else:
                prod[i] = prod[i-1] * nums[i]
        
        for i in range(len(nums)-1,-1, -1):
            if i == len(nums)-1:
                rev_prod[i] = nums[i]
            else:
                rev_prod[i] = rev_prod[i+1]*nums[i]
        
        for i in range(len(nums)):
            if i == 0:
                res[i] = rev_prod[1]
            elif i == len(nums)-1:
                res[i] = prod[i-1]
            else:
                res[i] = prod[i-1]*rev_prod[i+1]
        
        return res

        