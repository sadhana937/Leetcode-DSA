# Boyer-Moore Majority Vote Algorithm 
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        majority_ele = nums[0] 
        for i in range(1,len(nums)):
            if majority_ele == nums[i]:
                count += 1
            elif count == 0:
                majority_ele = nums[i]
                count = 1
            else:
                count -= 1
        return majority_ele
