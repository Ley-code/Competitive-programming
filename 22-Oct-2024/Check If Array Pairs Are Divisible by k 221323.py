# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        pairs = defaultdict(int)
        for num in arr:
            mod = num%k
            if mod==0:
                if pairs[mod]:
                    pairs[mod]-=1
                else:
                    pairs[mod]+=1
            else:
                if k-mod in pairs and pairs[k-mod]>0:
                    pairs[k-mod]-=1
                else:
                    pairs[mod] += 1
        if sum(pairs.values())==0:
            return True
        return False
