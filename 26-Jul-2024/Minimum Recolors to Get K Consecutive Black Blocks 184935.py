# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        hashmap = Counter(blocks[:k-1])
        miniOp = float('inf')
        l = 0
        for r in range(k-1,len(blocks)):
            hashmap[blocks[r]]+=1
            miniOp = min(miniOp,hashmap["W"])
            hashmap[blocks[l]]-=1
            if hashmap[blocks[l]]==0:
                del hashmap[blocks[l]]
            l+=1
        return miniOp