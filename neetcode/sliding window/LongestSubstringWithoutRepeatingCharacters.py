class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        currStr = 0;
        currLen = 0;
        maxLen = 0;
        strset = set()
        while j < len(s) and i < len(s):
            currStr = s[j]
            if currStr in strset:
                strset.remove(s[i])
                i = i + 1
                currLen -= 1
                continue
            strset.add(currStr)
            j += 1
            currLen += 1
            maxLen = max(currLen, maxLen)
        return maxLen