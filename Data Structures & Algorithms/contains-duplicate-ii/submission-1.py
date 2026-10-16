class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        l = 0
        nums_set = set()
        
        for r in range(len(nums)):
            if r - l > k:
                nums_set.remove(nums[l])
                l += 1
            if nums[r] in nums_set:
                return True 
            else:
                nums_set.add(nums[r])
        return False
