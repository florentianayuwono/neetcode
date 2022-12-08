class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        for i in s:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        for j in t:
            if j in a:
                a[j] -= 1
            else:
                return False
        return all(item == 0 for item in a.values())