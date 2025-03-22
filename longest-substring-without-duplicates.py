class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        res = 1
        i,j = 0,1
        dic = dict()
        dic[s[0]]=0
        while j<n:
            if s[j] in dic:
                i = dic[s[j]]+1
            dic[s[j]] = j
            j+=1
            count = j-i
            res = max(res,count)
        return res

            

            