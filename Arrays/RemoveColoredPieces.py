'''
The problem involves a game with a line of colored pieces, 'A' and 'B', where Alice and Bob take turns removing pieces. Alice can remove 'A' pieces if both neighboring pieces are also 'A', and Bob can remove 'B' pieces under the same condition. Return True if Alice wins the game or False if Bob wins.
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count = 0
        for i in range(len(colors)-2):
            if colors[i:i+3] == 'AAA':
                count += 1
            elif colors[i:i+3] == 'BBB':
                count -= 1
        return True if count > 0 else False
