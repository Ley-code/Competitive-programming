class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counterMap = {}
        for index in range(len(cpdomains)):
            values = cpdomains[index].split()
            visited = int(values[0])
            address = values[1].split(".")
            for i in range(len(address)):
                possibleName = ".".join(address[i:])
                if possibleName in counterMap:
                    counterMap[possibleName]+= visited
                else:
                    counterMap[possibleName] = visited
        result = []
        for domain,visits in counterMap.items():
            ans = str(visits) + " " + domain
            result.append(ans)
        return result

