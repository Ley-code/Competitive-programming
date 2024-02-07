class Solution(object):
    from collections import Counter
    def subarraysDivByK(self, nums, k):
        hashmap = Counter()
        hashmap[0] = 1
        cur_sum = answer = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            mod = cur_sum % k
            answer += hashmap[mod]
            hashmap[mod]+=1
        return answer