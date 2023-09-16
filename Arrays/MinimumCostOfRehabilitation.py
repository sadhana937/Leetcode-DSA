'''
Find the minimum cost of rehabilitation where A is the array of prices for a session on the certain day, X is the number of sessions need to be 
assigned and Y is the number of days that has to be maintained between two sessions.
Time complexity: O(n^2) (Not an optimal algorithm)
Space complexity: O(n)
'''
def solution(A, X, Y):
    N = len(A)
    x = [A[i] for i in range(0, N, Y)]
    minimum_cost = sum(x[:X])

    for i in range(1, N):
        x = [A[j] for j in range(i, N, Y)]
        cur_sum = sum(x[:X])
        if minimum_cost > cur_sum and len(x) >= X:
            minimum_cost = cur_sum
    return minimum_cost
