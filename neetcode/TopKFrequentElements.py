class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = dict()
        keep = [[] for i in range(len(nums) + 1)]
        for num in nums:
            if num in ans:
                ans[num] += 1
            else:
                ans[num] = 1
        for key, value in ans.items():
            keep[value].append(key)
        
        result = []
        for i in range(len(keep)):
            if len(result) >= k:
                return result
            pos = len(keep) - i - 1
            if keep[pos] != []:
                for j in keep[pos]:
                    result.append(j)