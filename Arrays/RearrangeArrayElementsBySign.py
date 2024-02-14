class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [i for i in nums if i > 0]
        negative = [i for i in nums if i < 0]
        n = len(nums)
        i = 0
        j = 0
        while i < n:
            nums[i] = positive[j]
            nums[i + 1] = negative[j]
            i += 2
            j += 1
        return nums
