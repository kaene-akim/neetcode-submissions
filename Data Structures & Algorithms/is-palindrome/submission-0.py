class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        a = 0
        b = len(cleaned) - 1

        while a < b:
            if cleaned[a] != cleaned[b]:
                return False
            a += 1
            b -= 1

        return True