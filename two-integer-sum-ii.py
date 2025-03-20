class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        sum = numbers[i]+numbers[j]
        while sum < target:
            j+=1
            sum = numbers[i]+numbers[j]
        if sum == target:
            return [i+1,j+1]
        while sum == target:
            if numbers[i]+numbers[j] > target:
                j-=1
            else:
                i+=1
            sum = numbers[i]+numbers[j]
        return [i+1,j+1]

        