import heapq
class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        _dict = dict()
        i,j = 0, 0
        max_freq = 0
        max_len = 0

        while j < len(s):
            _dict[s[j]] = 1 + _dict.get(s[j], 0)
            if (j-i+1) - max(_dict.values()) > k:
                _dict[s[i]] = _dict.get(s[j], 0) - 1
                i+=1
            max_len = max(max_len, j-i+1)
            j+=1
        return max_len





      



