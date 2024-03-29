class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        count = 0
        max_count = 0
        for i in numset:
            if (i - 1) not in numset:
                length = 1
                while (i + length) in numset:
                    length += 1
                max_count = max(max_count, length)
        return max_count



            

            
