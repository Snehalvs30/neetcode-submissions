class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        uniq = list(set(nums))
        freq = []

        for num in uniq:
            count = nums.count(num)
            freq.append((count, num))
            
        freq.sort()

        result=[]
        for i in range(k):
            result.append(freq[-k+i][1])
        return result
            
            
        