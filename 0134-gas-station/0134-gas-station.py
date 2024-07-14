class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        my_gas = 0
        index = 0
        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_cost > total_gas:
            return -1

        for i in range(len(gas)):
            my_gas += gas[i] - cost[i]
            if my_gas < 0:
                my_gas = 0
                index = i + 1
        return index
                

        