class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        result = 0
        strSet = {}
        maxFreq = 0
        for r in range(len(s)):
            strSet[s[r]] = 1 + strSet.get(s[r], 0)
            maxFreq = max(maxFreq, strSet[s[r]])
            while (r - l + 1) - maxFreq > k:
                strSet[s[l]] -= 1
                l += 1  
            result = max(r - l + 1, result)
        return result
