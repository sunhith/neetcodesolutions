class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = 1 + dic.get(num , 0)
        sorted_dic_values = sorted(dic.items(),key= lambda item:item[1], reverse = True)

        res = []
        for item in sorted_dic_values:
            res.append(item[0])
            if len(res) == k:
                break
        return res