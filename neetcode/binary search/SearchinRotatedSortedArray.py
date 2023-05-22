class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start < end:
            middle = start + (end - start)//2
            if target == nums[middle]:
                return middle
            if nums[start] <= nums[end]:
                # min is on the left side
                if target <= nums[middle]:
                    end = middle
                else:
                    start = middle + 1
            else:
                # min is on the right side
                if nums[middle] >= nums[start]:
                    if target >= nums[middle] or target <= nums[end]:
                        start = middle + 1
                    else:
                        end = middle
                else:
                    if target >= nums[middle] and target <= nums[end]:
                        start = middle + 1
                    else:
                        end = middle
        if target == nums[start]:
            return start
        return -1
