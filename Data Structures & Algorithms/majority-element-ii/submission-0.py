class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        for num in count:
            if count[num] > len(nums) // 3:
                result.append(num)

        return result