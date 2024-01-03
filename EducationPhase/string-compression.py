class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []
        l = 0
        r = 0 
        i = 0
        while r<len(chars):
            if chars[r]!=chars[l]:
                chars[i] = chars[l]
                i+=1   
                if r-l > 1:
                    length = str(r-l)
                    for j in range(len(length)):
                        chars[i] = length[j]
                        i+=1
                l = r
            r+=1
        chars[i] = chars[l]
        i+=1
        if r-l > 1:
            length = str(r-l)
            for k in range(len(length)):
                chars[i] = length[k]
                i+=1
        return i
            