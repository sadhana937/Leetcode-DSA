class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        prefix = [0] * (n + 1)
        mod = 10 ** 9 + 7
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        subarraysum = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                subarraysum.append(prefix[j] - prefix[i])
        subarraysum.sort()
        return sum(subarraysum[left - 1: right]) % mod
