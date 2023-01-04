class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        resultLen = len(s) + 1
        resultId = [0, 0]

        check = {}
        for i in range(len(t)):
            check[t[i]] = 1 + check.get(t[i], 0)
        checkLen = len(check)

        haveSoFar = {}
        haveLen = len(haveSoFar)

        for r in range(len(s)):
            haveSoFar[s[r]] = 1 + haveSoFar.get(s[r], 0)
            if s[r] in check and haveSoFar[s[r]] == check[s[r]]:
                haveLen += 1
            
            while haveLen >= checkLen:
                if r - l + 1 < resultLen:
                    resultId = [l, r]
                    resultLen = r - l + 1
                haveSoFar[s[l]] -= 1
                if s[l] in check and haveSoFar[s[l]] < check[s[l]]:
                    haveLen -= 1
                l += 1

        if resultLen < len(s) + 1:
            return s[resultId[0]:resultId[1] + 1]
        else:
            return ""
