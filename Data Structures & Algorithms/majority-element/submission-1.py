class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      key = 0
      candidate = 0
      for num in nums:
         if key == 0:
            candidate = num
         if candidate == num:
            key += 1
         else:
            key -= 1
      return candidate