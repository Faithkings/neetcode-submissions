class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        num_map = {}

        for i, num in enumerate(nums):
            needed_num = target - num
            
            if needed_num in num_map:
                return[num_map[needed_num], i]

            num_map[num] = i 
            



