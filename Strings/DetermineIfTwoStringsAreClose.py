class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        list1 = []
        list2 = []

        if set(word1) != set(word2):
            return False

        alphabet = list(set(word1))

        for i in alphabet:
            list1.append(word1.count(i))
            list2.append(word2.count(i))

        list1.sort()
        list2.sort()

        return list1 == list2
