class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        rep = []
        for num in nums:
            if num in rep:
                return True
            rep.append(num)

        return False
             
            
