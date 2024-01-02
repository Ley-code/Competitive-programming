class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        minimumTime = 0
        tasks.sort()
        processorTime.sort(reverse=True)
        for i in range(len(processorTime)):
            minimumTime = max(minimumTime,processorTime[i]+tasks[4*(i+1)-1])
        return minimumTime