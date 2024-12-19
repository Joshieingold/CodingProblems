class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        record = []
        while numBottles != 0:
            count = 0
            currency = numBottles
            while currency > 0:
                currency -= numExchange
                count += 1
            record.append(count)
            numBottles = record[-1]
        return sum(record)
                