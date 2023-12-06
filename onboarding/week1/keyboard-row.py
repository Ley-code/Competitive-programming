class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        american = []
        for word in words:
            count1 = 0
            count2 = 0
            count3 = 0
            for i in range(len(word)):
                if word[i].lower() in "qwertyuiop":
                    count1+=1
                elif word[i].lower() in "asdfghjkl":
                    count2+=1
                else:
                    count3+=1
            if count1 == len(word) or count2 == len(word) or count3 == len(word):
                american.append(word)
        return american
            