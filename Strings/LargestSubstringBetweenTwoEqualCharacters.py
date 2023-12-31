class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        index = defaultdict(list)
        for i, char in enumerate(s):
            index[char].append(i)
            
        max_count = -1
        cur_count = -1
        
        for i in s:
            cur_count = index[i][-1] - index[i][0] - 1
            max_count = max(cur_count, max_count)

        return max_count
