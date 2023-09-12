#  Brute force approach
Time complexity: O(n)
Space complexity: O(1)
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]


# Two pointer technique
# Time complexity: O(n)
# Space complexity: O(1)
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        
        
