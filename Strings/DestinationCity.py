class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = []
        n = len(paths)
        for i in range(n):
            source.append(paths[i][0])

        for i in range(n):
            if paths[i][1] not in source:
                return paths[i][1]
