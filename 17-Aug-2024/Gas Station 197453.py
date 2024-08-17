# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        tot = 0
        startidx = 0
        for i in range(len(gas)):
            if tot<0:
                tot=0
                startidx = i
            tot+= diff[i]
        return startidx
                