# Rotating an array to the right by k steps
# Time complexity: O(n)
# Space complexity: O(1) 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        n = len(nums) - k
        nums[:n] = nums[:n][::-1]
        nums[n:] = nums[n:][::-1]
        nums.reverse()
