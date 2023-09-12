def reverser(sentence):
    newsentence = ""
    halfway = len(sentence)//2
    for i in range(halfway,len(sentence)):
        newsentence+= (sentence[i]+" ")
    for i in range(halfway):
        newsentence+=(sentence[i]+" ") 
    return newsentence
sentence = list(map(str,input().split()))
print(reverser(sentence))