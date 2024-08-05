class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        unique_count = 0
        for key, value in count.items():
            if value == 1:
                unique_count += 1
            if unique_count == k:
                return key
        return ""
