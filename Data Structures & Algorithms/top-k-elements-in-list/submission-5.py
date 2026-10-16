
from collections import defaultdict, Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        output= []
        frequency = Counter(nums)
        result = frequency.most_common(k)
        for i in range(len(result)):
            output.append(result[i][0])
        return output
        


        

        