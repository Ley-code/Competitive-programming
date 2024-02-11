class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        prefixsum = {}
        suffixsum = {}
        for i in range(len(nums)):
            if nums[i] in prefixsum:
                prev = prefixsum[nums[i]]
                first = prev[0] + (i-prev[1])*prev[2]
                second = i
                third = prev[2]+1
                prefixsum[nums[i]] = [first,second,third]
                ans[i] += first
            else:
                prefixsum[nums[i]] = [0,i,1]
        nums.reverse()
        ans2 = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] in suffixsum:
                prev = suffixsum[nums[i]]
                first = prev[0] + (i-prev[1])*prev[2]
                second = i
                third = prev[2]+1
                suffixsum[nums[i]] = [first,second,third]
                ans2[i] += first
            else:
                suffixsum[nums[i]] = [0,i,1]
        ans2.reverse()
        for i in range(len(nums)):
            ans[i]+=ans2[i]
        return ans 
        """indexmap   = {}
        ans = [0]*len(nums)    
        for i in range(len(nums)):
            indexmap[nums[i]] = indexmap.get(nums[i],[])+[i]
        for i in range(len(nums)):
            values = indexmap[nums[i]]
            sums = 0
            for j in range(len(values)):
                sums+=abs(values[j]-i)
            ans[i] = sums
        return ans
        """