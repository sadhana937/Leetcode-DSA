class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count_of_chars = defaultdict(int)
        for i in range(len(words)):
            for j in range(len(words[i])):
                count_of_chars[words[i][j]] += 1

        ref = len(words)
        for val in count_of_chars.values():
            if val % ref != 0:
                return False
        return True
