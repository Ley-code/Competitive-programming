class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        minops = 0
        for count in hashmap.values():
            if count==1:
                return -1
            elif count>2:
                if count%3 == 1 or count%3 == 2:
                    minops+=1
                minops += count//3
            elif count==2:
                minops+=1
        return minops
        