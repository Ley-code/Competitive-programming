class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        hashmap = {}
        for i in range(len(order)):
            hashmap[order[i]] = i
        l,r= 0,1
        while r<len(words):
            k = 0
            mini = min(len(words[l]),len(words[r]))
            while k < mini and r<len(words):
                idx1 = hashmap[words[l][k]]
                idx2 = hashmap[words[r][k]]
                if idx1==idx2:
                    k+=1
                elif idx1>idx2:
                    return False
                else:
                    break
            if k == mini:
                if len(words[l])>len(words[r]):
                    return False
            l+=1
            r+=1
        return True
                