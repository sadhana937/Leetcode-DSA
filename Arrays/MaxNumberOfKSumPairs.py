# Max Number of K-Sum Pairs - Two pointers method
# Time complexity: O(nlogn)
# Space complexity: O(1)

class Solution1:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        count = 0
        while i < j:
            x = nums[i] + nums[j]
            if x < k:
                i += 1
            elif x > k:
                j -= 1
            else:
                count += 1
                i, j = i + 1, j - 1
        return count
      

# Time complexity: O(n)
# Space complexxity: O(1)
# from collections import defaultdict
class Solution2:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        dictionary = defaultdict(int) 
        for i in nums:
            if dictionary[i] > 0:
                dictionary[i] -= 1
                count += 1
            else:
                dictionary[k - i] += 1
        return count        
            










