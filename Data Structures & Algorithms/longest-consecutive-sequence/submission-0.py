class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for number in numbers:
            if number - 1 not in numbers:      # number is the start of a run
                i = 0
                while number + i in numbers:   # count up: number, number+1, ...
                    i += 1
                longest = max(longest, i)

        return longest