class Solution(object):
    def minimumRecolors(self, blocks, k):
        colormap ={"B":0,"W":0}
        l,i = 0,0
        min_op = len(blocks)+1
        while i < len(blocks):
            colormap[blocks[i]] +=1
            if i >= k-1:
                min_op = min(min_op,colormap["W"])
                colormap[blocks[l]]-=1
                l+=1
            i+=1
        return min_op
            