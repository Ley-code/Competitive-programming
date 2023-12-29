class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newnums = sorted(nums)
        arr = []
        nummap = {}
        for i,x in enumerate(newnums):
            if x in nummap:
                continue
            nummap[x] = i
        for i in range(len(nums)):
            arr.append(nummap[nums[i]])
        return arr


