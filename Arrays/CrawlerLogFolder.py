class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for i in logs:
            if i == "./":
                continue
            elif i == "../":
                count -= 1
                count = max(count, 0)
            else:
                count += 1
        return count
