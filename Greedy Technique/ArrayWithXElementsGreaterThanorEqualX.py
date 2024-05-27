class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = [0] * (len(nums) + 1)

        for num in nums:
            if num < len(nums):
                count[num] += 1
            else:
                count[-1] += 1

        total = 0
        for i in range(len(nums), -1, -1):
            total += count[i]
            if total == i:
                return i

        return -1
