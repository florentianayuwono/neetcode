class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start < end:
            middle = start + (end - start)//2
            if nums[start] <= nums[end]:
                # min is on left side
                end = middle
            else:
                # min is on right side
                if nums[middle] <= nums[end]:
                    end = middle
                else:
                    start = middle + 1
        return nums[start]
