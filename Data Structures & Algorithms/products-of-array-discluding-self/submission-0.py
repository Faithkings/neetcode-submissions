class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left_size = 1 
        right_size = 1
        
        for i in range(len(nums)):
            result[i]= left_size
            left_size *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right_size
            right_size *= nums[i]

        return result
