class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str not in dic:
                dic[sorted_str] = [string]
            else:
                lis = dic[sorted_str]
                lis.append(string)
                dic[sorted_str] = lis
        lis = []
        for d in dic:
            lis.append(dic[d])
        return lis