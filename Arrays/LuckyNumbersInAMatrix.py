class Solution1:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_min = [min(row) for row in matrix]
        col_max = [max(col) for col in zip(*matrix)]

        return [num for num in row_min if num in col_max]

class Solution2:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min = []
        for i in matrix:
            row_min.append(min(i))
        
        max_col = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] > max_col[j]:
                    max_col[j] = matrix[i][j]

        return list(set(row_min) & set(max_col))
