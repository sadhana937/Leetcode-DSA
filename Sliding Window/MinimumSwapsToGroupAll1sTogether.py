class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count1 = nums.count(1)
        count0 = nums[:count1].count(0)
        output = count0
        nums_extended = nums + nums
        for i in range(1, len(nums)):
            if nums_extended[i - 1] == 0:
                count0 -= 1
            if nums_extended[i + count1 - 1] == 0:
                count0 += 1
            output = min(output, count0)
        return output
