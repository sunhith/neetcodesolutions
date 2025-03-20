class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       res = []
       nums.sort()
       print("sorted")
       n = len(nums)
       for i in range(len(nums)):
        print(i)
        print(nums[i])
        if i!=0 and nums[i] ==a:
            continue 
        a = nums[i]
        print(a)
        j = i + 1
        k = n-1
        while(j < k):
            if a + nums[j]+nums[k] > 0:
                k-=1
            elif a + nums[j]+nums[k] < 0:
                j+=1
            else:
                res.append([a,nums[j],nums[k]])
                i+=1
                j+=1
       return res

