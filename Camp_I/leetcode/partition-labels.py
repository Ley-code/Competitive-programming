class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {v:i for i,v in enumerate(s)}
        part = [mp[s[0]]]
        for i in range(len(s)):
            if mp[s[i]]>part[-1] and i<=part[-1]:
                part[-1] = mp[s[i]]
            elif mp[s[i]]>part[-1] and i>part[-1]:
                part.append(mp[s[i]])
        newp = [part[0]+1]
        for i in range(len(part)):
            if i>0:
                newp.append(part[i]-part[i-1])
        return newp
        