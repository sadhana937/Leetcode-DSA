class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            start_index = nums.index(target)
        except ValueError:
            return [-1,-1]
        end_index = start_index
        for i in range(start_index,len(nums)):
            if nums[i] == target:
                end_index = i
            else:
                break
        return [start_index,end_index]
