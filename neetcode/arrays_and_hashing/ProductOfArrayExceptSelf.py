class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(len(nums) - 1):
                result[i + 1] = result[i] * nums[i]
        post = 1
        for i in range(len(nums)):
            pos = len(nums) - i - 1
            post = post * nums[pos]
            if pos > 0:
                result[pos - 1] = post * result[pos - 1]
        return result
'''
nums = [1, 2, 3, 4]
result = [1, 1, 2, 6]
result = [24, 12, 8, 6]
'''