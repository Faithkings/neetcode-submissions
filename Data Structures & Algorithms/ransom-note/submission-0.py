from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        r_map = defaultdict(int)

        for i in ransomNote:
            r_map[i] += 1

        for j in magazine:
            if r_map.get(j):
                r_map[j] -= 1
            elif not r_map.get(j):
                continue
        if sum(r_map.values()) == 0:
            return True
        else:
            return False