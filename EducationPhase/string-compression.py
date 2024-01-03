class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        i = 0
        count = 0
        for r in range(len(chars)):
            if chars[l]==chars[r]:
                count+=1
            else:
                chars[i] = chars[l]
                i+=1
                if count>1:
                    length = str(count)
                    for j in range(len(length)):
                        chars[i] = length[j]
                        i+=1
                count = 1
                l=r
        chars[i] = chars[l]
        i+=1
        if count>1:
            length = str(count)
            for j in range(len(length)):
                chars[i] = length[j]
                i+=1
        return i