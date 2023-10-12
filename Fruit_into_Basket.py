class Solution(object):
    def totalFruit(self, fruits):
        fruitmap = {}
        l,total,res = 0,0,0
        for i in range(len(fruits)):
            if fruits[i] in fruitmap:
                fruitmap[fruits[i]]+=1
            else:
                fruitmap[fruits[i]] = 1
            total+=1
            while len(fruitmap) > 2:
                fruitmap[fruits[l]]-=1
                total-=1
                if fruitmap[fruits[l]] == 0:
                    fruitmap.pop(fruits[l])
                l+=1
            res = max(total,res)
        return res

            