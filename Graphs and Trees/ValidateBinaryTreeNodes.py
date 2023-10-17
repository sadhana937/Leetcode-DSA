# DFS
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        children = set(leftChild + rightChild)
        root = -1
        visited = []
        stack = []
        for i in range(n):
            if i not in children:
                root = i
        if root == -1:
            return False
        visited.append(root)
        stack.append(root)
        while stack:
            vertex = stack.pop()
            for i in (leftChild[vertex], rightChild[vertex]):
                if i != -1:
                    if i in visited:
                        return False
                    else:
                        stack.append(i)
                        visited.append(i)
        if n == len(visited):
            return True
        else:
            return False
