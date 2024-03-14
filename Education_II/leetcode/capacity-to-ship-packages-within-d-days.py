class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(targetsum):
            runningsum = 0
            count = 0
            for i in range(len(weights)):
                runningsum+=weights[i]
                if runningsum > targetsum:
                    count+=1
                    runningsum=weights[i]
                elif runningsum == targetsum:
                    count+=1
                    runningsum = 0
            if runningsum:
                count+=1
            return count
        low,high = max(weights),sum(weights)
        while low<=high:
            mid = low + (high-low)//2
            if check(mid)>days:
                low = mid+1
            else:
                high = mid-1
        return low
                
