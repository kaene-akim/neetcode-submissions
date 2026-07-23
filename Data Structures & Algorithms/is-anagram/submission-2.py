class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for char in s:
            num = s.count(char)
            num2 = t.count(char)
            if num != num2:
                return False
            if char not in t:
                return False

        return True