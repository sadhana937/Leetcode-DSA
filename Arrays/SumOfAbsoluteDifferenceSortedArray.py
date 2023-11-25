class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [abs(sum(nums[1:]) - (n - 1) * nums[0])]
        cf = [nums[0]]
        for i in range(1, n):
            cf.append(cf[i - 1] + nums[i])
        print(cf)
        for i in range(1, n):
            left = abs(cf[i - 1] - (i * nums[i]))
            right = abs((cf[n - 1] - cf[i]) - ((n - i - 1) * nums[i]))
            result.append(left + right)
        return result
