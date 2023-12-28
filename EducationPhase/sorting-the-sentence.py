class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        arr.sort(key = lambda x:x[-1])
        for i,word in enumerate(arr):
            arr[i] = word[:len(word)-1]
        return " ".join(arr)