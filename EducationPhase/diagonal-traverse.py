class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        ans = []
        sameIdxSum = {}
        for i in range(rows):
            for j in range(cols):
                sameIdxSum[i+j] = sameIdxSum.get(i+j,[])+[mat[i][j]]
        for idx,ele in sameIdxSum.items():
            if idx%2==0:
                ans += ele[::-1]
            else:
                ans+= ele
        return ans


        