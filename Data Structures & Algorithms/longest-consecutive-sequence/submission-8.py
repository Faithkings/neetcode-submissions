class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # nums = sorted(nums)
        # length_count = 1

        # i = 0
        # while i + 1 < len(nums):
        #     if nums[i + 1] == nums[i] + 1:
        #         length_count += 1
        #     i += 1

        # return length_count

        if not nums:
            return 0

        nums = set(nums)
        longest = 0
        count = 0

        for num in nums:
            if num - 1 not in nums:
                count = 1 
                while num + count in nums:
                    count += 1
                longest = max(longest, count)
        return longest

            
            