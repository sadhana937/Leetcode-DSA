class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for i in nums:
            if i in visited:
                return True
            else:
                visited.add(i)
        return False

