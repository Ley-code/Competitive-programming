class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        totsum = sum(nums)
        if totsum%p == 0:
            return 0
        if totsum<p:
            return -1
        indexmap = {0:-1}
        currsum = 0
        remainder = totsum%p
        mini = len(nums)
        for i in range(len(nums)):
            currsum+=nums[i]
            if (currsum-remainder)%p in indexmap:
                mini = min(mini,i-indexmap[(currsum-remainder)%p])
            indexmap[currsum%p] = i 
        return mini if mini < len(nums) else -1