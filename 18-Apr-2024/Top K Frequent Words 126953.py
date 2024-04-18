# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = Counter(words)
        heap = []
        for word in hashmap:
            heapq.heappush(heap,[-hashmap[word],word])
        ans=[]
        while k>0:
            cnt,word = heapq.heappop(heap)
            ans.append(word)
            k-=1
        return ans
