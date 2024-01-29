class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        maps = {}
        count = 0
        morsecode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in range(len(words)):
            morse = ""
            for c in words[i]:
                idx = ord(c)-97
                print(idx)
                morse+=morsecode[idx]
            if morse in maps:
                continue
            else:
                count+=1
                maps[morse]=1
        return count
