class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        hashmap = {}
        maxlen = 0
        highestFreq = 0
        l = 0
        for i in range(len(answerKey)):
            hashmap[answerKey[i]] = hashmap.get(answerKey[i],0)+1
            highestFreq = max(highestFreq,hashmap[answerKey[i]])
            while ((i-l+1) - highestFreq) >k:
                hashmap[answerKey[l]] -=1
                highestFreq = max(hashmap["T"],hashmap["F"])
                l+=1
            maxlen = max(maxlen,i-l+1)
        return maxlen                