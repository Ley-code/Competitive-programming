class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        lengthS1,lengthS2,lengthS3 = len(s1),len(s2),len(s3)
        if s1[0]!=s2[0] or s1[0]!=s3[0] or s2[0]!=s3[0]:
            return -1
        i,j,k = 0,0,0
        while i<lengthS1 and j<lengthS2 and k<lengthS3:
            if s1[i]!=s2[j] or s1[i]!=s3[k] or s2[j]!=s3[k]:
                break
            i+=1
            j+=1
            k+=1
        return (lengthS1-i +lengthS2-j + lengthS3-k)