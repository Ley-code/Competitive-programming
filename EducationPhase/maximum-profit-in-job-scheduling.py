class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        tasks = []
        for i in range(n):
            tasks.append((startTime[i], 1, i))
            tasks.append((endTime[i], 0, i))
        tasks.sort()        
        maxProfit = [0]*n
        previousMax = 0
        
        for time, eventType, index in tasks:
            if eventType == 1:
                maxProfit[index] = previousMax + profit[index]

            else:
                previousMax = max(maxProfit[index], previousMax)
            
        return previousMax