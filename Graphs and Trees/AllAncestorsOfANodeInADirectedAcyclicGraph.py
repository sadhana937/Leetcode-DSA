class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        output = []

        for i, j in edges:
            graph[j].append(i)

        for i in range(n):
            ancestors = set()
            visited = set()
            queue = deque([i])

            while queue:
                cur = queue.popleft()
                for parent in graph[cur]:
                    if parent not in visited:
                        visited.add(parent)
                        queue.append(parent)
                        ancestors.add(parent)
            
            output.append(sorted(ancestors))

        return output
