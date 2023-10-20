class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        nummap = {}
        for idx,num in enumerate(nums):
            if num not in nummap:
                nummap[num] = idx
            else:
                if abs(idx-nummap[num]) <=k:
                    return True
                else:
                    nummap[num] = idx
        return False