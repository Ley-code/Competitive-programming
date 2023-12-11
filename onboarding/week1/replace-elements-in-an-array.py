class Solution(object):
    def arrayChange(self, nums, operations):
        hashmap = {}
        for i,x in enumerate(nums):
            hashmap[x] = i
        for x,y in operations:
            index = hashmap[x]
            nums[index] = y
            hashmap[y] = index
            del hashmap[x]
        return nums