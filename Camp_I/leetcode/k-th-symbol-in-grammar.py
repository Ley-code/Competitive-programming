class Solution(object):
    def kthGrammar(self, n, k):
        if n == 1:
            return 0
        parent = self.kthGrammar(n-1,k/2 + k%2)
        isodd = k%2==1
        if parent == 1:
            return 1 if isodd else 0
        else:
            return 0 if isodd else 1
    
        