class Solution(object):
    def checkSubarraySum(self, nums, k):
        lookup = {0:-1}
        curr_sum = 0
        
        for i, n in enumerate(nums):
            curr_sum = (curr_sum + n) % k
            if curr_sum not in lookup:
                lookup[curr_sum] = i
            elif i - lookup[curr_sum] > 1:
                    return True
        return False