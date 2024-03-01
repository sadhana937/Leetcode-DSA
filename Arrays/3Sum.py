class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                theSum = nums[i] + nums[j] + nums[k]
                if theSum == 0:
                    output.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif theSum < 0:
                    j += 1
                else:
                    k -= 1
                
        return list(output)
