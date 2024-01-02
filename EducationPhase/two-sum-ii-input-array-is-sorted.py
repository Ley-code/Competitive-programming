class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers)-1
        while left<right:
            sumation = numbers[left]+numbers[right]
            if sumation > target:
                right-=1
            elif sumation < target:
                left+=1
            else:
                return [left+1,right+1]
            

        