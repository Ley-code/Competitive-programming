# Problem: Word Ladder - https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        graph = defaultdict(list)
        n = len(beginWord)
        for word in wordList:
            for i in range(n):
                transformed = word[:i]+"*"+word[i+1:]
                graph[transformed].append(word)
        q = deque([[beginWord,1]])
        visited =set([beginWord])
        while q:
            word,depth = q.popleft()
            for i in range(n):
                transformed = word[:i]+"*"+word[i+1:]
                for neighbor in graph[transformed]:
                    if neighbor==endWord:
                        return depth+1
                    if neighbor not in visited:
                        q.append([neighbor,depth+1])
                        visited.add(neighbor)
        return 0