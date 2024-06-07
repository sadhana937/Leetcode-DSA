class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        words = sentence.split()
        output = []

        for word in words:
            flag = False
            for i in range(len(word) + 1):
                cur = word[:i]
                if cur in dictionary:
                    output.append(cur)
                    flag = True
                    break
            if not flag:
                output.append(word)
        
        return " ".join(output)
