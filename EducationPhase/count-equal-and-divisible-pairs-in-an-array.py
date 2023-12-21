class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        indiceMap = {}
        count = 0
        for idx,num in enumerate(nums):
            if num in indiceMap:
                for i in range(len(indiceMap[num])):
                    if (idx* indiceMap[num][i]) % k == 0:
                        count+=1
            indiceMap[num] = indiceMap.get(num,[])+[idx]
        return count