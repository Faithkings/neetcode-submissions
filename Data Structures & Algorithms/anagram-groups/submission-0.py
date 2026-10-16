from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        word_map = defaultdict(list)
        result = []

        for s in strs:
            sorted_words = tuple(sorted(s))
            word_map[sorted_words].append(s)

        for values in word_map.values():
            result.append(values)

        return result

