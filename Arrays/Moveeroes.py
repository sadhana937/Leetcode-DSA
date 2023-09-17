# Time complexity: O(n)
# Space complexity: O(1)
class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)

# Two pointer method
# Time complexity: O(n)
# Space complexity: O(1)
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        if 0 in nums:
            j = 0
            i = nums.index(0)
            for j in range(len(nums)):
                if i < j and nums[i] == 0 and nums[j] != 0:
                    nums[i] , nums[j] = nums[j] , nums[i]
                    i += 1      
