class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        count1 = Counter(s1)
        for word in s2:
            count1[word] += 1
        
        output = []
        for key, val in count1.items():
            if val == 1:
                output.append(key)
        return output
