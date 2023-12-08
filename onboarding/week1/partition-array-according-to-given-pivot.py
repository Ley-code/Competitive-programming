class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessthan,equal,morethan = [],[],[]
        for num in nums:
            if num>pivot:
                morethan.append(num)
            elif num==pivot:
                equal.append(num)
            else:
                lessthan.append(num)
        return lessthan+equal+morethan