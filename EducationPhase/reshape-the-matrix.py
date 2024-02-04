class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        oned = []
        for i in range(len(mat)):
            oned.extend(mat[i])
        ans = []
        n = len(oned)
        if n < r*c or n>r*c:
            return mat
        for i in range(0,n,c):
            ans.append(oned[i:i+c])
        return ans