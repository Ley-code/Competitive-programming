class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        rightB = n-1
        leftB = 0
        bottomB = m-1
        topB = 0
        i,j = 0,0
        count = 0
        ans = []
        size = m*n
        while count < (size):
            while count<size and j<=rightB:
                count+=1
                ans.append(matrix[i][j])
                j+=1
            j-=1
            i+=1
            topB+=1
            while count<size and i<=bottomB:
                count+=1
                ans.append(matrix[i][j])
                i+=1
            i-=1
            j-=1
            rightB-=1
            while count<size and j>=leftB:
                ans.append(matrix[i][j])
                count+=1
                j-=1
            j+=1
            i-=1
            bottomB-=1
            while count<size and i>=topB:
                ans.append(matrix[i][j])
                count+=1
                i-=1
            i+=1
            j+=1
            leftB+=1
        return ans