class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        result = 0
        currLen = 0
        strSet = {}
        for r in range(len(s)):
            currLen = r - l + 1
            strSet[s[r]] = 1 + strSet.get(s[r], 0)
            currFreq = max(strSet.values())
            while currLen - currFreq > k:
                print(strSet[s[l]])
                strSet[s[l]] -= 1
                l += 1
                
            result = max(currLen, result)
        return result
