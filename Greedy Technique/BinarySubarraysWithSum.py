class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        output = 0
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        sum_count = defaultdict(int)
        for i in prefix_sum:
            output += sum_count[i]
            sum_count[i + goal] += 1

        return output
