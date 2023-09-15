# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j