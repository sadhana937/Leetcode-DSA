class Solution1:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]

class Solution2:
    def findCenter(self, edges: List[List[int]]) -> int:
        hash_map = defaultdict(int)
        for i , j in edges:
            hash_map[i] += 1
            hash_map[j] += 1
        
        return max(hash_map, key = lambda k: hash_map[k])
      
