class Solution:
    def printVertically(self, s: str) -> List[str]:
        maxlength = 0
        for word in s.split():
            maxlength = max(len(word),maxlength)
        hashmap = {num:"" for num in range(maxlength)}
        for word in s.split():
            for j in range(maxlength):
                if j>len(word)-1:
                    hashmap[j]+=" "
                else:
                    hashmap[j]+=word[j]
        array = []
        #appends to the array with right striping
        for element in hashmap:
            array.append(hashmap[element].rstrip())
        return array
            