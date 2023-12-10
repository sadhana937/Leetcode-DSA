class Solution1:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_row = len(matrix[0])
        new_column = len(matrix)
        transpose = [[0] * new_column for _ in range(new_row)]
        for i in range(new_row):
            for j in range(new_column):
                transpose[i][j] = matrix[j][i]
        return transpose

class Solution2:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

class Solution3:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)
