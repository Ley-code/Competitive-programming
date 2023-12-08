class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        stack=[nums[0]]
        for i in range(1,len(nums)):
            if stack[-1]>nums[i]:
                count+=1
                if count>=2:return False
                y=stack.pop()
                if stack:
                    if stack[-1]>nums[i]:
                        stack+=[y]
                        continue

            stack+=[nums[i]]
        return True