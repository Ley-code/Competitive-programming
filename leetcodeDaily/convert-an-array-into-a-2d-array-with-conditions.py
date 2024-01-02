class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        array2d = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                array2d[hashmap[nums[i]]] = array2d.get(hashmap[nums[i]],[])+[nums[i]]
                hashmap[nums[i]] = hashmap.get(nums[i],0)+1
            else:
                array2d[0] = array2d.get(0,[])+[nums[i]]
                hashmap[nums[i]] = hashmap.get(nums[i],0)+1
        return array2d.values()