class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_v2 = []
        string = ""
        for i in digits:
            string += str(i)
        string = int(string)
        string = string + 1 
        string = str(string)
        for j in string:
            digits_v2.append(int(j))
        return(digits_v2)