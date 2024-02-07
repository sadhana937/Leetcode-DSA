class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s)
        output = []
        for key, value in count.most_common():
            output += [key] * value
            
        return "".join(output)
