class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}      # total -> how many times we've seen it
        total = 0
        counter = 0

        for num in nums:
            total += num
            counter += seen.get(total - k, 0)
            seen[total] = seen.get(total, 0) + 1

        return counter