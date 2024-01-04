class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = defaultdict(int)
        output = 0
        for i in nums:
            count[i] += 1
        for i in count.keys():
            if count[i] == 1:
                return -1
            output += count[i] // 3
            count[i] %= 3
            if count[i] > 0:
                output += 1
        return output
