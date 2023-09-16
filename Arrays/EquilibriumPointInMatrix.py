# Time complexity: O(mn)
# Space complexity: O(m + n)

def Solution(A):
    N = len(A)
    M = len(A[0])

    row_sum = [[0] * M for _ in range(N)]
    col_sum = [[0] * M for _ in range(N)]

    equilibrium_point = []
    # finding the cumulative sum for rows and columns
    for i in range(N):
        for j in range(M):
            row_sum[i][j] = A[i][j] + (row_sum[i][j-1] if j > 0 else 0)
            col_sum[i][j] = A[i][j] + (col_sum[i-1][j] if i > 0 else 0)

    for i in range(N):
        for j in range(M):
            left_sum = row_sum[i][j - 1] if j > 0 else 0
            right_sum = row_sum[i][M - 1] - row_sum[i][j]
            above_sum = col_sum[i - 1][j] if i > 0 else 0
            below_sum = col_sum[N - 1][j] - col_sum[i][j]

            if left_sum == right_sum and above_sum == below_sum:
                equilibrium_point.append([i,j])
    return equilibrium_point

  
