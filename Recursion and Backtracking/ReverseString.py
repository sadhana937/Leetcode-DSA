class Solution1:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recursion(i, j):
            if i > j:
                return 
            s[i], s[j] = s[j], s[i]
            recursion(i + 1, j - 1)
        
        recursion(0, len(s) - 1)


class Solution2:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
