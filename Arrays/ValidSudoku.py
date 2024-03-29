class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited = set()
        squares = defaultdict(set)

        # checking rows
        for i in range(9):
            visited.clear()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in visited:
                        return False
                    visited.add(board[i][j])
        
        # checking cols
        for i in range(9):
            visited.clear()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in visited:
                        return False
                    visited.add(board[j][i])

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in squares[(i // 3, j // 3)]:
                        return False
                    squares[(i // 3, j // 3)].add(board[i][j])
        return True
