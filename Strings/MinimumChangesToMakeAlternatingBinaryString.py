class Solution:
    def minOperations(self, s: str) -> int:
        operations_from_beginning = 0
        operations_from_end = 0
        prev = 0
        for i in s:
            if int(i) != prev:
                operations_from_beginning += 1
            prev = not prev
            
        operations_from_end = len(s) - operations_from_beginning

        return min(operations_from_beginning, operations_from_end)
