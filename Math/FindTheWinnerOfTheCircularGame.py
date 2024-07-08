class Solution2:
    def findTheWinner(self, n: int, k: int) -> int:
        # if we know the winner of (n, k) we can find the winner of (n + 1, k) by (winner(n, k) + k) % (n + 1)
        winner = 0
        for i in range(2, n + 1):
            winner = (winner + k) % i
        return winner + 1

class Solution1:
    def findTheWinner(self, n: int, k: int) -> int:
      # Just a brute force approach really, count the kth element and pop it or else append it at the end of the queue
        friends = [i for i in range(1, n + 1)]
        cur =  1
        while len(friends) > 1:
            if cur == k:
                friends.pop(0)
                cur = 1
            else:
                num = friends.pop(0)
                friends.append(num)
                cur += 1
        return friends[0]

    
