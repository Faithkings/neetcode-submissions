class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        s_set = set()
        res = 0

        for r in range(len(s)):
            while s[r] in s_set:
                s_set.remove(s[l])
                l += 1 
            if s[r] not in s_set:
                s_set.add(s[r])
            length = r - l + 1
            res = max(length, res)
        return res


            

