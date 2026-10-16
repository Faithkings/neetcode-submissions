class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # stable = []
        # ttable = []

        # for letter in s:
        #     stable.append(letter)

        # for letter in t:
        #     ttable.append(letter)

        # stable.sort()
        # ttable.sort()

        # if stable == ttable:
        #     return True
        # else:
        #     return False

        s_map = {}
        t_map = {}

        for s_l in s:
            if s_l not in s_map:
                s_map[s_l] = 1
            elif s_l in s_map:
                s_map[s_l] += 1

        for t_l in t:
            if t_l not in t_map:
                t_map[t_l] = 1
            elif t_l in t_map:
                t_map[t_l] += 1
        
        if s_map.items() == t_map.items():
            return True
        else:
            return False
        


        