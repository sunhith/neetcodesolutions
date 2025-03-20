class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       res = []
       nums.sort() # .sort() is mutable sorted() is immutable
       n = len(nums)
       for i in range(len(nums)):
        if i!=0 and nums[i] == a:
            continue 
        a = nums[i]
        j = i + 1
        k = n-1
        while(j < k):
            if a + nums[j]+nums[k] > 0:
                k-=1
            elif a + nums[j]+nums[k] < 0:
                j+=1
            else:
                res.append([a,nums[j],nums[k]])
                b = nums[j]
                while(j<k and nums[j+1] == b):
                    j+=1
                j+=1
                k-=1
       return res

