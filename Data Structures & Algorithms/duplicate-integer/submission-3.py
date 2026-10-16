
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # rep = []
        # for num in nums:
        #     if num in rep:
        #         return True
        #     rep.append(num)

        # return False
             
            
        nums_map = dict()

        for i in nums:
            if i not in nums_map:
                nums_map[i] = 1
            elif i in nums_map:
                nums_map[i] += 1
        for i in nums_map.values():
            if i > 1:
                return True
        return False
        