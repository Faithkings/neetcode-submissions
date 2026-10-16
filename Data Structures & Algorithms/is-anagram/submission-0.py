class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stable = []
        ttable = []

        for letter in s:
            stable.append(letter)

        for letter in t:
            ttable.append(letter)

        stable.sort()
        ttable.sort()

        if stable == ttable:
            return True
        else:
            return False

        


        