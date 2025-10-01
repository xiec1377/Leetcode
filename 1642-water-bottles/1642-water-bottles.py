class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drankBottles = 0
        while numBottles >= numExchange:
            drankBottles += numExchange
            numBottles -= numExchange
            numBottles += 1
        return drankBottles + numBottles
        

        