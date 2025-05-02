import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dic = {}
        # # get the frequency of list
        # for num in nums:
        #     dic[num] = 1 + dic.get(num , 0)
        # # sort the dictionary based on the frequency in descending order
        # sorted_dic_values = sorted(dic.items(),key= lambda item:item[1], reverse = True) 
        
        # res = []
        # for item in sorted_dic_values:
        #     res.append(item[0])
        #     if len(res) == k:
        #         break
        # return res

        dic = defaultdict(int)
        for num in nums:
            dic[num] = 1 + dic[num]
        
        heap = []
        for key in dic.keys():
            heapq.heappush(heap, (dic[key],key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

