class Solution1:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums2 = set(nums2)
        for i in nums1:
            if i in nums2:
                return i
        return -1


class Solution2:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)
        common = nums1.intersection(nums2)
        if common:
            return min(common)
        else:
            return -1

