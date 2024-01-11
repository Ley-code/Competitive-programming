class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxlen = 0
        fruitsmap = defaultdict(int)
        l = 0
        for r in range(len(fruits)):
            fruitsmap[fruits[r]]+=1
            while len(fruitsmap)>2:
                fruitsmap[fruits[l]]-=1
                if fruitsmap[fruits[l]] == 0:
                    del fruitsmap[fruits[l]]
                l+=1
            maxlen = max(maxlen,r-l+1)
        return maxlen