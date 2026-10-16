from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        

        s_map = defaultdict(int)

        for i in s:
            s_map[i] += 1

        # for j in s_map.keys():
        #     if s_map[j] == 0:
        #         break
        for index, j in s_map.items():
            if j == 1:
                return s.index(index)
        return -1