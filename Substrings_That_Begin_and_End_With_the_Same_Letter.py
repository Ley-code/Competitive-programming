def SubstringsThatBeginandEndWiththeSameLetter(s):
    lettermap = {}
    count = 0
    for r in range(len(s)):
        if s[r] in lettermap:
            count+= lettermap[s[r]]
        count+=1
        lettermap[s[r]] = lettermap.get(s[r],0)+1
    return count
print(SubstringsThatBeginandEndWiththeSameLetter("a"))
