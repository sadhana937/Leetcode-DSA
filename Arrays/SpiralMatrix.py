class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        m = len(matrix)
        n = len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        while left <= right and top <= bottom:
            
            # Traversing right
            for i in range(left, right + 1):
                output.append(matrix[top][i])
            top += 1
            
            # Traversing down
            for i in range(top, bottom + 1):
                output.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # Traversing left
                for i in range(right, left - 1, -1):
                    output.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                # Traversing up
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])
                left += 1
            
            
        
        return output
                
