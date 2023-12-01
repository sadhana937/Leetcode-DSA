# Time complexity: O(m + n)
# Space complexity: O(m + n)
class Solution1:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ''.join(word1)
        str2 = ''.join(word2)
        if str1 != str2:
            return False
        else:
            return True


# Time complexity: O(min(m, n))
# Space complexity: O(1)
class Solution2:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for a, b in zip(self.generate(word1), self.generate(word2)):
            if a != b:
                return False
        return True

    def generate(self, wordlist):
        for word in wordlist:
            for char in word:
                yield char
        yield None
