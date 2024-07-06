class Solution1:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = (n - 1) * 2  # One full back and forth pass
        time %= cycle_length  # Reduce time to within one full cycle
        
        # Determine the current position based on the reduced time
        if time < n - 1:
            return 1 + time  # Forward direction
        else:
            return n - (time - (n - 1))  # Backward direction

class Solution2:
    def passThePillow(self, n: int, time: int) -> int:
        cur = 1
        direction = False
        while time > 0:
            if cur == 1:
                direction = False
                cur += 1
            elif cur == n:
                direction = True
                cur -= 1
            elif direction:
                cur -= 1
            else:
                cur += 1
            time -= 1
        return cur
        

        
