'''
- Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
- Time complexity: O(n)
- Space complexity: O(1)
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i[::-1] for i in s.split()])
        
