# Two pointer approach
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if (nums[i] % 2) != 0:
                while i < j and (nums[j] % 2) != 0:
                    j -= 1
                nums[i] , nums[j] = nums[j] , nums[i]
            i += 1
        return nums
                
