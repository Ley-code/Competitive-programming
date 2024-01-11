class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        colorcount = Counter(blocks[:k-1])
        r= k-1
        l = 0
        minicolor = len(blocks)+1
        while r<len(blocks):
            colorcount[blocks[r]]+=1
            minicolor = min(colorcount["W"],minicolor)
            colorcount[blocks[l]]-=1
            l+=1
            r+=1
        return minicolor