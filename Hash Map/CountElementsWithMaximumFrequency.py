class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_count = max(count.values())
        return max_count * list(count.values()).count(max_count)
