# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = defaultdict(int)
        for word in dictionary:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = defaultdict(int)
                curr = curr[c]
            curr["is_end"] = True
        sentence = sentence.split()
        res  = []
        for word in sentence:
            curr = trie
            ans = ""
            flag = False
            for c in word:
                if c in curr and curr[c]["is_end"]:
                    res.append(ans+c)
                    ans+=c
                    flag = True
                    break
                if c not in curr:
                    ans = ""
                    flag = True
                    break
                ans+= c
                curr = curr[c]
            if ans == "" or not flag:
                res.append(word)
        return " ".join(res)
