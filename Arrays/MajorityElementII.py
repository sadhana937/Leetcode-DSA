# Boyer-Moore Majority Voting Algorithm
# Time complexity: O(n)
# Space complexity: O(1)
# Runtime - 108 ms, Memory - 17.79 MB
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        result = []
        num1, num2 = 0, 1
        count1, count2 = 0, 0
        for i in nums:
            if i == num1:
                count1 += 1
            elif i == num2:
                count2 += 1
            elif count1 == 0:
                num1 = i
                count1 = 1
            elif count2 == 0:
                num2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        for i in (num1, num2):
            if nums.count(i) > n:
                result.append(i)
        return result

'''
#Time complexity: O(n)
#space complexity: O(n)
# Runtime - 9320 ms, Memory - 17.80 MB
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {i : nums.count(i) for i in nums}
        n = len(nums) // 3
        result = []
        for key in count:
            if count[key] > n:
                result.append(key)
        return result        

# Time complexity: O(n^2)
# space complexity: O(n/3)
# Runtime - 104 ms, Memory - 17.80 MB
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        result = []
        for i in nums:
            if i not in result:
                if nums.count(i) > n:
                    result.append(i)
        return result
'''
