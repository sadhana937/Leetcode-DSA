class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        integer_value = roman_to_int[s[0]]
        for i in range(1,len(s)):
            if roman_to_int[s[i-1]] < roman_to_int[s[i]]: 
                integer_value = integer_value + roman_to_int[s[i]] - 2 * roman_to_int[s[i-1]]
            else:
                integer_value += roman_to_int[s[i]]
        return integer_value
