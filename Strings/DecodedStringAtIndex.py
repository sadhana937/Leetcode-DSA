# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoded_str_length = 0
        # Finding the length of the decoded string
        for i in s:
            if i.isdigit():
                decoded_str_length *= int(i)
            else:
                decoded_str_length += 1
        
        s = s[::-1]

        for i in s:
            k %= decoded_str_length 
            if i.isdigit():
                decoded_str_length //= int(i) # reducing the length by no. of repetitions done when an integer is encountered
            elif k == 0:
                return i 
            else:
                decoded_str_length -= 1 # reducing the length by one as a character is encountered

            
