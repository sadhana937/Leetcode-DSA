class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        summ = 0
        maxlen = 0
        prefix_sum = {0 : -1}
        for i, val in enumerate(nums):
            if val == 1:
                summ += 1
            else:
                summ -= 1
            if summ not in prefix_sum:
                prefix_sum[summ] = i
            else:
                maxlen = max(maxlen, i - prefix_sum[summ])

        return maxlen
