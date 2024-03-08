class Solution1:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        deleted = False
        i = 1
        prev = nums[0]
        while i < len(nums):
            if not deleted and nums[i] <= prev:
                deleted = True
                if i == 1 or nums[i] > nums[i - 2]:
                    prev = nums[i]
                i += 1
            elif deleted and nums[i] <= prev:
                return False
            else:
                prev = nums[i]
                i += 1
        return True

class Solution2:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed = False
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                if removed:
                    return False
                if i > 1 and nums[i] <= nums[i - 2]:
                    nums[i] = nums[i - 1]
                removed = True
        return True

