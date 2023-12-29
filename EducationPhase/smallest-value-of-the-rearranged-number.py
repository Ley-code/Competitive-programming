class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = str(abs(num))
        nums = [nums[i] for i in range(len(nums))]
        print(nums)
        if num>0:
            nums.sort()
            for i in range(len(nums)):
                if nums[0]=="0" and nums[i]!="0":
                    nums[i],nums[0] = nums[0],nums[i]
                    break
        else:
            nums.sort(reverse = True)
        return int("-"+"".join(nums)) if num<0 else int("".join(nums))

                      