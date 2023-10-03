'''
Given an array of integers nums, return the number of good pairs. A pair (i, j) is called good if nums[i] == nums[j] and i < j.
Time complexity: O(n)
Space complexity: O(n)
'''
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {i: nums.count(i) for i in nums}
        good_pairs = 0
        for value in count.values():
                good_pairs += value *(value - 1) / 2
        return int(good_pairs)
