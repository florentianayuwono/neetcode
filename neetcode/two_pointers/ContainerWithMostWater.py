class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        firstPointer = 0
        secondPointer = len(height) - 1

        while firstPointer < secondPointer:
            currArea = min(height[firstPointer], height[secondPointer]) * (secondPointer - firstPointer)
            result = max(result, currArea)
            if height[firstPointer] > height[secondPointer]:
                secondPointer -= 1
            else:
                firstPointer += 1
        return result