class Solution:
    def isPalindrome(self, x: int) -> bool:
        sequence=str(x)
        result=sequence[::-1]
        if sequence==result:
            return True
        else:
            return False
