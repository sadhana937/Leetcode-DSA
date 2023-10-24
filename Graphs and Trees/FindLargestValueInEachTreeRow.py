# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            max_value = float('-inf')
            total_nodes = len(queue)
            for i in range(total_nodes):
                cur_node = queue.popleft()
                if cur_node.val > max_value:
                    max_value = cur_node.val
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

            result.append(max_value)
        return result
