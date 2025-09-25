class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_surplus, surplus, start, n = 0, 0, 0, len(gas)

        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]

            if surplus < 0:
                surplus = 0
                start = i + 1

        return -1 if total_surplus < 0 else start