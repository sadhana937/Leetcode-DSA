class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = Counter(nums1)
        output = []
        for i in nums2:
            if hashmap[i] > 0:
                output.append(i)
                hashmap[i] -= 1
        return output
        
class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        common = set1.intersection(set2)
        output = []
        for i in common:
            count = min(nums1.count(i), nums2.count(i))
            while count > 0:
                output.append(i)
                count -= 1
        return output
