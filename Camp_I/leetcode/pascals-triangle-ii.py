class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=  [[1]]
        i = 0
        while i < rowIndex:
            temp = [0]+res[-1]+[0]
            row = []
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
            i+=1
        return res[-1]