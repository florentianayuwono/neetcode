class Solution:
    def isPalindrome(self, s: str) -> bool:
        firstPtr = 0
        secondPtr = len(s) - 1

        while firstPtr < len(s):
            if s[firstPtr].lower() == s[secondPtr].lower():
                firstPtr += 1
                secondPtr -= 1
            elif not s[firstPtr].isalnum():
                firstPtr += 1
            elif not s[secondPtr].isalnum():
                secondPtr -= 1
            else:
                return False
        return True