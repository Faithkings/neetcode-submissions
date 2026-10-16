class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l = 0
        r = 0
        string = []

        while l < len(word1) and r < len(word2):
            string.append(word1[l])
            string.append(word2[r])
            l += 1
            r += 1
        if len(word1) == l and len(word2) != r:
            string.append(word2[r:len(word2)])
        elif len(word2) == r and len(word1) != l:
            string.append(word1[r:len(word1)])

        return ''.join(string)
        