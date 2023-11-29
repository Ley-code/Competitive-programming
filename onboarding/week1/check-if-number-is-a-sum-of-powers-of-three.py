class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n!=0:
            digit = n%3
            if digit == 2:
                return False
            n = n//3
        return True


            
         
        