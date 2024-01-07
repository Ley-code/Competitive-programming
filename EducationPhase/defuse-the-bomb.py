class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans=[]
        s=0
        if k==0:
            ans = [0]*len(code)
        else:
            absK=abs(k)
            s=sum(code[0:absK])
            for i in range(len(code)):
                s=s-code[i]+code[(i+absK)%len(code)]
                ans.append(s)
            if k<0:
                ans=ans[k-1:]+ans[:k-1]
        return ans
