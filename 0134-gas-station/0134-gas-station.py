class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        totalGas = 0
        start = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            # print("gas[i]:", gas[i])
            totalGas += gas[i] - cost[i]
            if totalGas < 0:
                # restart loop
                totalGas = 0
                start = i + 1

        return start

        