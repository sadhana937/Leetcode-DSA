class Solution1:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinkable = numBottles
        drunk = 0
        empty = 0
        while drinkable:
            drunk += drinkable
            empty += drinkable
            drinkable = empty // numExchange
            empty %= numExchange
        
        return drunk
            

class Solution2:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)
