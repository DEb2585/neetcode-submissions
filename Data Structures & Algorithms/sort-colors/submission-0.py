class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1       # pass 1: count each color

        k = 0                     # write pointer
        for color in range(3):    # colors 0, 1, 2 in order
            for _ in range(count[color]):   # repeat it count times
                nums[k] = color
                k += 1