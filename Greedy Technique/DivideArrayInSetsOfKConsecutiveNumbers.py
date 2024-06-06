class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        nums.sort()
        count = Counter(nums)

        for num in nums:
            if count[num] > 0:
                for i in range(k):
                    if count[num + i] > 0:
                        count[num + i] -= 1
                    else:
                        return False
        return True
