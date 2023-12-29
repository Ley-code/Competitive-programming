class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        array2d = [[0]*n for _ in range(m)]
        array2d1 = [[0]*n for _ in range(m)]
        hashmap = {}   
        for x,y in walls:
            hashmap[(x,y)]  = 1
            array2d[x][y] = "H"
            array2d1[x][y] = "V"
        for i,j in guards:
            x,y = i,j
            array2d[i][j] = "H"
            array2d1[i][j] = "V"
            while j<n-1 and (i,j) not in hashmap and array2d[i][j+1]!="H" :
                array2d[i][j+1] = "H"
                j+=1
            i,j = x,y
            while j>0 and (i,j) not in hashmap and array2d[i][j-1]!="H":
                array2d[i][j-1] = "H"
                j-=1
            i,j = x,y
            while i>0 and (i,j) not in hashmap and array2d1[i-1][j]!="V":
                array2d1[i-1][j] = "V"
                i-=1
            i,j = x,y
            while i<m-1 and (i,j) not in hashmap and array2d1[i+1][j]!="V":
                array2d1[i+1][j] = "V"
                i+=1
        count = 0
        for k in range(m):
            for l in range(n):
                if array2d[k][l]==array2d1[k][l] and array2d1[k][l]==0:
                    count+=1
        '''for k in range(m):
            for l in range(n):
                if array2d[k][l] == 0:
                    pass
                print(array2d[k][l],end="")
            print()
        '''
        return count
        
                        


                