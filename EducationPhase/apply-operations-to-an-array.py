class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        def movezeroes(res):
            write = 0
            read = 0
            while read<len(nums):
                if res[read]!=0:
                    res[read],res[write]=res[write],res[read]
                    write+=1
                read+=1
            return  res
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        return movezeroes(nums)