class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        counter = 1
        while counter<n:
            pote = ""
            l = 0
            r= 0 
            while r<len(ans):
                if ans[r]!= ans[l]:
                    count = r-l
                    char = ans[l]
                    pote+= str(count)+char
                    l = r
                r+=1
            pote+=str(r-l)+ans[-1]
            print(pote)
            ans = pote
            counter+=1
        return ans