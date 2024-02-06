class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new = defaultdict(list)
        for string in strs:
            chars = tuple(sorted(string))
            new[chars].append(string)
        return list(new.values())
