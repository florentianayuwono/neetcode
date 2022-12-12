class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        inspect = set(nums)
        length = 0
        for num in inspect:
            # start of sequence
            if not num - 1 in inspect:
                start = num
                curr_length = 1
                while start + 1 in inspect:
                    curr_length += 1
                    start = start + 1
                if curr_length > length:
                    length = curr_length
        return length