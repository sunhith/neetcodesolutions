class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlen = 1
        curlen = 1
        for num in nums:
            if num-1 not in numset:
                 # that could be a start of a sequence
                while (num + curlen) in numset:
                    curlen+=1
            maxlen = max(curlen, maxlen)
            curlen =1
        return maxlen



            
        