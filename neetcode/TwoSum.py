class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s= dict()
        for i in range(len(nums)):
            s[i] = nums[i]
        for a in s:
            if target - s[a] in s.values():
                pos = list(s.values()).index(target - s[a])
                if pos != a:
                    return [a, pos]