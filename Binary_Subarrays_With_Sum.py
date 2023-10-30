class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        '''[1,0,1,0,1]
                    ^
            1 1 2 2 3
            {1:2,2:2,3:1}
         '''
        prefixsum = 0
        count = 0
        hashMap = {}
        for num in nums:
            prefixsum+=num
            if prefixsum == goal:
                count+=1
            if prefixsum-goal in hashMap:
                count+=hashMap[prefixsum-goal]
            hashMap[prefixsum] = hashMap.get(prefixsum,0)+1
        return count