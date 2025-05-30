class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = defaultdict(int)
        res = 0
        for i in range(len(s1)):
            freq[s1[i]] = 1 + freq[s1[i]]
        l,r = 0,0
        while r < len(s2):
            if s2[r] in freq:
                if freq[s2[r]] > 0:
                    freq[s2[r]] = freq[s2[r]] - 1
                    r+=1
                else:
                    while l<=r:
                        freq[s2[l]] = freq[s2[l]]+1
                        l+=1
                    r+=1
            else:
                while l<r:
                    freq[s2[l]] = freq[s2[l]]+1
                    l+=1
                l+=1
                r+=1

            if len(s1) == r-l:
                return True
        return False
        