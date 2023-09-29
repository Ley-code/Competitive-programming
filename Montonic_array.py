class solution:
    def ismontonic(nums):
        isincreasing = True
        isdecreasing = True
        for i in range(len(nums)-1):
            if nums[i+1] >= nums[i]:
                isdecreasing = False
            elif nums[i+1] <= nums[i]:
                isincreasing = False
        if isincreasing or isdecreasing:
            return True
        return False