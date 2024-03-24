class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        l = 0
        while l<len(arr):
            correctpos = int(arr[l][-1])-1
            if correctpos!=l:
                arr[l],arr[correctpos] = arr[correctpos],arr[l]
            else:
                l+=1
        for i,word in enumerate(arr):
            arr[i] = word[:len(word)-1]
        return " ".join(arr)