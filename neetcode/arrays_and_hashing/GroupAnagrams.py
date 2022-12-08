class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            temp = [0] * 26
            for char in s:
                temp[ord(char) - ord("a")] += 1
            ans[tuple(temp)].append(s)
        return ans.values()