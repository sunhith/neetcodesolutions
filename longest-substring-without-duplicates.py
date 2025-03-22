class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        TC- O(n)- We traverse the string once using the two-pointer technique.
        SC- O(m)- m is the number of unique characters in the substring
        It uses a dictionary to store the last seen index of characters and adjusts the left 
        pointer (i) whenever a duplicate is found with an index + 1.
        """
        n = len(s)
        if n == 0:
            return 0
        res = 1
        i,j = 0,1
        dic = dict()
        dic[s[0]]=0
        while j < n:
            if s[j] in dic and dic[s[j]]>=i:
                i = dic[s[j]]+1
            dic[s[j]] = j
            j+=1
            count = j-i
            res = max(res,count)
        return res

        """
        Same Logic as above code
        mp = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
        """

            

            