class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        firstPointer = 0
        leftPointer = firstPointer + 1
        rightPointer = len(nums) - 1
        while firstPointer < len(nums) and nums[firstPointer] <= 0:
            while leftPointer < rightPointer:
                total = nums[leftPointer] + nums[rightPointer]
                if total + nums[firstPointer] == 0:
                    toAdd = [nums[firstPointer], nums[leftPointer], nums[rightPointer]]
                    result.add(tuple(toAdd))
                    leftPointer += 1
                elif total + nums[firstPointer] < 0:
                    leftPointer += 1
                else:
                    rightPointer -= 1
            firstPointer += 1
            leftPointer = firstPointer + 1
            rightPointer = len(nums) - 1
        return result