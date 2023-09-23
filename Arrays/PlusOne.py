class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = "".join(str(i) for i in digits)
        string = str(int(string) + 1)
        return [int(i) for i in string]
