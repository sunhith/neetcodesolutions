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
