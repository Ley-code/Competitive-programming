class Solution(object):
    def singleNumber(self, nums):
        onelist=[]
        for i in nums:
            if i not in onelist:
                onelist.append(i)
            else:
                onelist.remove(i)
        return onelist[0]