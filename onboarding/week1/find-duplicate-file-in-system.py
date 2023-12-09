class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        result = []
        hashmap = {}
        for sent in paths:
            sentsplit = sent.split()
            for i in range(len(sentsplit)):
                value = sentsplit[0]+"/"
                if i>0:
                    length = len(sentsplit[i])
                    for j in range(length):
                        if sentsplit[i][j] == "(":
                            keys = "".join(sentsplit[i][j+1:length-1])
                            value += sentsplit[i][:j]
                            hashmap[keys] = hashmap.get(keys,[])+[value]
        for key in hashmap:
            if len(hashmap[key])>1:
                result.append(hashmap[key])
        return result
                
